# Glimmer-and-Gloom
A python automated bot to play Flight Rising's Glimmer and Gloom minigame.

Intended for split-screen usage on a 1920x1080p monitor at normal zoom. Although it may function at different resolutions, the boundaries may have to be tweaked.

Run bot.py when the game has begun, as in the screenshot:
<img src="https://i.imgur.com/4VFS5As.jpg">

The bot will work its way, clicking down from the top left to the bottom right. When it runs out of gloom hexes that aren't on the bottom right edges, it'll calculate the appropriate glimmers to click on and work them down to cancel out the remaining edge hexes. Calculations from the excellent <a href="https://docs.google.com/spreadsheets/d/1zrLIjer2FKmknXpyopCSEfVDdEP5rgxWsTOBVFkW8lQ/edit#gid=0">spreadsheet</a> done by <a href="https://flightrising.com/main.php?p=lair&tab=userpage&id=186567">Sqld</a>.

If at any time the program has to be stopped, move your cursor to the corner of the screen. That will terminate the project.

The bulk of this project was made possible by <a href="https://github.com/drov0">drov0</a>'s <a href="https://github.com/drov0/python-imagesearch">python-imagesearch</a> project, and includes his imagesearch.py file with some minor edits. 

# Installation
- Download the files.
- You need python, and then several dependencies which can be installed via running `pip install -r requirements.txt`.
- Run the file in splitscreen!
