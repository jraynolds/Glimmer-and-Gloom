# Plays indefinitely.

import pyautogui
import time
from board_solver import *

PLAY_FILE_LOC = "play.png" # The local file location of the play button image
GAME_DELAY = 2 # How much we wait before starting a new game.
CONFIDENCE_VALUE = .9 # The confidence value we're searching the screen with. A lower number will lead to more false positives.

while(True):
	print("beginning a run...")
	time.sleep(GAME_DELAY)
	solve_board()
	time.sleep(GAME_DELAY)
	pyautogui.click(
		pyautogui.center(
			pyautogui.locateOnScreen(
				PLAY_FILE_LOC, 
				confidence=CONFIDENCE_VALUE
			)
		)
	)
	print("ending a run...")