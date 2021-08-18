# Glimmer-and-Gloom
A python automated bot to play Flight Rising's Glimmer and Gloom minigame.

Intended for split-screen usage on a 1920x1080p monitor at normal zoom. Although it may function at different resolutions, the boundaries may have to be tweaked.

Run bot.py when the game has begun, as in the screenshot:
<img src="https://i.imgur.com/4VFS5As.jpg">

The bot will work its way, clicking down from the top left to the bottom right. When it runs out of gloom hexes that aren't on the bottom right edges, it'll calculate the appropriate glimmers to click on and work them down to cancel out the remaining edge hexes. Calculations from the excellent <a href="https://docs.google.com/spreadsheets/d/1zrLIjer2FKmknXpyopCSEfVDdEP5rgxWsTOBVFkW8lQ/edit#gid=0">spreadsheet</a> done by <a href="https://flightrising.com/main.php?p=lair&tab=userpage&id=186567">Sqld</a>.

If at any time the program has to be stopped, move your cursor to the corner of the screen. That will terminate the project.

The bulk of this project was made possible by <a href="https://github.com/drov0">drov0</a>'s <a href="https://github.com/drov0/python-imagesearch">python-imagesearch</a> project, and includes his imagesearch.py file with some minor edits. 

# Quick guide
- Download the files.
- You need python, and then several dependencies which can be installed via running `pip install -r requirements.txt`.
- Run the file in splitscreen!

# Step-by-step guide
- Download the files (click on the green code button, download as a .zip, and unzip it using WinRar or similar)
- Install python (https://www.python.org/downloads/)
- Open the unzipped folder, click the Windows Explorer location bar, type 'cmd' and press enter
- Type `pip install -r requirements.txt` in the resulting window and press enter
- Arrange your Glimmer and Gloom game to the left side of your screen
- Make sure the global variable `DEBUG_MODE` in `bot.py` is set to `True`. You can change it to False if everything is working fine; otherwise it'll give you valuable diagnostic information.
- Type `python bot.py` in that same cmd window and press enter
- It should work!
- Start a new game and do it again from `python bot.py`!

# Error handling
- Couldn't install python? Python help forums are better-equipped to assist than I.
- Requirements installing failed? Some of the code needed to run this program may have disappeared. That's out of my control.
- It fails with an array/tuple length objection? It's probably not capturing the right region. Make sure the DEBUG_MODE global variable is set to True, then run it and follow the diagnostic messages. This will save several images for you to check in your root project folder, e.g. Glimmer and Gloom/game_region.png. If you're not capturing the entire game region, you'll have to edit some of your global variables like GAME_OFFSET.
- Still not working? Please contact me on twitter @jasper_raynolds and let me know!
