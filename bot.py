from imagesearch import *
from numpy import empty

DEBUG_MODE = True # Set this to False once you're sure everything is working. When True, this will run a pretest to make sure everything is being detected as it should be and will print out diagnostic messages as you go.

CLICK_DELAY = .2

IMAGE_DIMENSIONS = (48, 31)

WINDOW_OFFSET = (220, 350)
GAME_DIMENSIONS = (720, 620)
GAME_PADDING = (100, 100)

ROW_DIMENSIONS = (485, 36)
ROW_MARGIN = 10

TOP_INDICES = [26, 18, 11, 5, 0, 1, 2, 3, 4]
BOTTOM_INDICES = [56, 57, 58, 59, 60, 55, 49, 42, 34]

BAN_EVASION_MODE = False # Introduces fuzzing to avoid cheat detection.
POINT_FUZZING_MAX = 3 # Fuzzes clicks by up to this number of pixels.
DELAY_FUZZING_MAX = .5 # Fuzzes click delay by up to this number of seconds.

GLIMMER_FILE_PATH = "./glimmer2.png"
GLOOM_FILE_PATH = "./gloom.png"

CAPTURE_REGION = (
	WINDOW_OFFSET[0] - GAME_PADDING[0], 
	WINDOW_OFFSET[1] - GAME_PADDING[0], 
	WINDOW_OFFSET[0] + GAME_DIMENSIONS[0] + GAME_PADDING[0], 
	WINDOW_OFFSET[1] + GAME_DIMENSIONS[1] + GAME_PADDING[1]
)

def run_bot():
	glimgloms = order_gloms(gather_gloms())

	while([g for g in glimgloms if g[2] == "gloom"]):
		if DEBUG_MODE:
			print("while started")
		while(click_lowest(glimgloms)):
			if DEBUG_MODE:
				print("clicking started.")
			glimgloms = order_gloms(gather_gloms())

		cells = solve_terminal([glimgloms.index(g) for g in glimgloms if g[2] == "gloom"])
		for cell in cells:
			if DEBUG_MODE:
				print(cell)
			click_cell(glimgloms[cell], False)

		glimgloms = order_gloms(gather_gloms())

def click_lowest(glimgloms):
	if DEBUG_MODE:
		print_board(glimgloms)

	glom = None
	for g in glimgloms:
		if g[2] == "gloom":
			if glimgloms.index(g) not in BOTTOM_INDICES:
				if DEBUG_MODE:
					print("We're clicking!")
				glom = g
				break

	if glom:
		click_cell(glom)
		return True
	else:
		return False

def click_cell(cell, clickingBottomRight=True):
	BOTTOM_RIGHT_OFFSET = [1, 2]
	DEFAULT_OFFSET = [.5, .5]
	offset = [DEFAULT_OFFSET[0], DEFAULT_OFFSET[1]]
	if clickingBottomRight:
		offset = [BOTTOM_RIGHT_OFFSET[0], BOTTOM_RIGHT_OFFSET[1]]

	x = WINDOW_OFFSET[0] + cell[0] + offset[0] * IMAGE_DIMENSIONS[0]
	y = WINDOW_OFFSET[1] + cell[1] + offset[1] * IMAGE_DIMENSIONS[1]
	if BAN_EVASION_MODE:
		x += random.randint(-POINT_FUZZING_MAX, POINT_FUZZING_MAX)
		y += random.randint(-POINT_FUZZING_MAX, POINT_FUZZING_MAX)

	pyautogui.moveTo(x, y)
	pyautogui.click(button="left")

	pauseAmount = CLICK_DELAY
	if BAN_EVASION_MODE:
		pauseAmount += random.uniform(0, DELAY_FUZZING_MAX)

	pyautogui.PAUSE = pauseAmount
	pyautogui.moveTo(30, 30)


def solve_terminal(gloom_indices):
	patterns = []
	patterns.append((0, 0, 0, 1, 0, 1, 0, 0, 1))
	patterns.append((0, 0, 0, 0, 1, 1, 1, 1, 0))
	patterns.append((0, 0, 1, 1, 0, 1, 0, 1, 0))
	patterns.append((1, 0, 1, 1, 0, 1, 1, 1, 1))
	patterns.append((0, 1, 0, 0, 1, 0, 0, 1, 0))
	patterns.append((1, 1, 1, 1, 0, 1, 1, 0, 1))
	patterns.append((0, 1, 0, 1, 0, 1, 1, 0, 0))
	patterns.append((0, 1, 1, 1, 1, 0, 0, 0, 0))
	patterns.append((1, 0, 0, 1, 0, 1, 0, 0, 0))
	if DEBUG_MODE:
		for row in patterns:
			print(row)
		print("")

	glooms = []
	for col in range(9):
		if BOTTOM_INDICES[col] in gloom_indices:
			glooms.append(1)
		else:
			glooms.append(0)
	if DEBUG_MODE:
		print(glooms)
		print("")

	checking = []
	for row in range(9):
		check_row = []
		for col in range(9):
			if BOTTOM_INDICES[row] in gloom_indices:
				check_row.append(patterns[row][col])
			else:
				check_row.append(0)
		checking.append(check_row)
	if DEBUG_MODE:
		for row in checking:
			print(row)
		print("")

	result = []
	for col in range(9):
		sum = 0
		for row in checking:
			sum += row[col]
		result.append(sum%2)
	if DEBUG_MODE:
		print(result)
		print("")

	cells = []
	for r in range(len(result)):
		if result[r] == 1:
			cells.append(TOP_INDICES[r])
	if DEBUG_MODE:
		print(cells)
		print("")

	return cells

def get_nw(pts):
	nw = pts[0]
	for pt in pts:
		if pt[1] < nw[1]:
			nw = pt
		elif pt[1] == nw[1] and pt[0] < nw[0]:
			nw = pt
	return nw

def gather_gloms():
	glimgloms = []
	glimmers = imagesearch_array(GLIMMER_FILE_PATH, CAPTURE_REGION)
	glooms = imagesearch_array(GLOOM_FILE_PATH, CAPTURE_REGION)

	for g in glimmers:
		glimgloms.append((g[0], g[1], "glimmer"))
	for g in glooms:
		glimgloms.append((g[0], g[1], "gloom"))
	if len(glimgloms) == 0:
		print("We didn't manage to find any glimmer or gloom squares. Is the game begun and visible on your screen?")
		print("Have you arranged the Flight Rising window and the search window area appropriately?")
	return glimgloms

def order_gloms(gloms):
	gloms.sort(key=lambda ord_glom: ord_glom[1])

	ordered_gloms = []
	row_gloms = []
	for i in range(9):
		glom = gloms[0]
		row_gloms = [g for g in gloms if abs(g[1] - glom[1]) < 5]
		new_gloms = []
		for r in row_gloms:
			if (r[0], glom[1], r[2]) not in new_gloms:
				new_gloms.append((r[0], glom[1], r[2]))
		gloms = [g for g in gloms if g not in row_gloms]
		new_gloms.sort(key=lambda ord_glom: ord_glom[0])
		ordered_gloms.extend(new_gloms)

	return ordered_gloms

def print_board(glimgloms):
	spacer = "      "

	board = []
	board.append([spacer, spacer, 0, 0, 0, 0, 0, spacer, spacer])
	board.append([spacer, 0, 0, 0, 0, 0, 0, spacer, spacer])
	board.append([spacer, 0, 0, 0, 0, 0, 0, 0, spacer])
	board.append([0, 0, 0, 0, 0, 0, 0, 0, spacer])
	board.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
	board.append([0, 0, 0, 0, 0, 0, 0, 0, spacer])
	board.append([spacer, 0, 0, 0, 0, 0, 0, 0, spacer])
	board.append([spacer, 0, 0, 0, 0, 0, 0, spacer, spacer])
	board.append([spacer, spacer, 0, 0, 0, 0, 0, spacer, spacer])

	if DEBUG_MODE:
		print("Length is " + str(len(glimgloms)))
		print(glimgloms)

def run_pretest():
	print("We're running a setup diagnostic.")
	im = region_grabber(region=CAPTURE_REGION)
	file_path = "game_region.png"
	print("We're saving a file to " + file_path + " showing our search region.")
	print("If the image you find at that location isn't representative of the entire game board, you need to change the global variables defining it.")
	im.save(file_path) # Saves a screenshot of the region we're looking in
	num_glimmers = imagesearch_count(
		GLIMMER_FILE_PATH, 
		CAPTURE_REGION, 
		save_output=" found", 
		debug=True
	)
	num_glooms = imagesearch_count(
		GLOOM_FILE_PATH, 
		CAPTURE_REGION, 
		save_output=" found", 
		debug=True
	)
	print("In total we found " + str(num_glimmers) + " glimmers and " + str(num_glooms) + " glooms.")

if DEBUG_MODE:
	run_pretest()
	run_bot()
else :
	run_bot()