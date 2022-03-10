# Glimmer-and-Gloom
A python automated bot to play Flight Rising's Glimmer and Gloom minigame on the Very Hard difficulty.

Run bot.py when the game has begun, as in the screenshot:
<img src="https://i.imgur.com/4VFS5As.jpg">

The bot will work its way, clicking down from the top left to the bottom right. When it runs out of gloom hexes that aren't on the bottom right edges, it'll calculate the appropriate glimmers to click on and work them down to cancel out the remaining edge hexes. Calculations from the excellent <a href="https://docs.google.com/spreadsheets/d/1zrLIjer2FKmknXpyopCSEfVDdEP5rgxWsTOBVFkW8lQ/edit#gid=0">spreadsheet</a> done by <a href="https://flightrising.com/main.php?p=lair&tab=userpage&id=186567">Sqld</a>.

If at any time the program has to be stopped, move your cursor to the top left corner of the screen and keep it there. That will terminate the project.

# Quick guide
- Download the files.
- You need python, and then several dependencies which can be installed via running `pip install -r requirements.txt`.
- Run `python board_solver.py` or `python autorun.py`!

# Step-by-step guide
- Download the files (click on the green code button, download as a .zip, and unzip it using WinRar or similar)
- Install python (https://www.python.org/downloads/)
- Open the unzipped folder, click the Windows Explorer location bar, type `cmd` and press enter
- Type `pip install -r requirements.txt` in the resulting window and press enter
- Make sure the Glimmer and Gloom game is started in Very Hard difficulty, and is visible on your screen.
- Type `python board_solver.py` in that same cmd window and press enter.
- It should work!
- If you want to keep it running, run `python autorun.py` instead!
- When you're done, or need to stop, move your mouse to the top left corner of your screen and keep it there. The mouse will move there periodically to help you reach it.

# Error handling
- Couldn't install python? Python help forums are better-equipped to assist than I.
- Requirements installing failed? Some of the code needed to run this program may have disappeared. That's out of my control.
- Keeps clicking the wrong thing? Make sure the command line is on the same screen.
- Fails with a "list index out of range" issue? Make sure the Very Hard game mode is visible on screen. Try with other web browsers too. If that fails, replace the image files with screenshot snips you've taken on your own computer.
- Not an above issue? Please open an Issue on this github project (or reply to one that matches your issue) and let me know!
