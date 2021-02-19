# PyCraft Launcher by ZachTheCoder

# Import libraries
import tkinter as tk
#from PIL import ImageTk, Image
import os

# Import settings data
import settingsData

# Check for updates
os.system("git pull")

# Set up the window
window = tk.Tk()
window.title("PyCraft Launcher")
window.iconbitmap("assets/icon.ico")
window.geometry("1000x900")
window.resizable(0,0)
window.configure(bg = "gray30")

# Create a title on the window
title = tk.Label(
    text = """
    PyCraft Launcher
    """,
    font = "Arial 12 bold",
    width = 1000,
    bg = "seashell4",
    fg = "white")
title.pack()

# Create a function that opens the launcher settings
def openSettings():
    os.system("python3 settings.py")

# Create a button for the launcher settings
settingsButton = tk.Button(
    text = "SETTINGS",
    font = "Arial 11 bold",
    width = 15,
    height = 4,
    bg = "green",
    fg = "white",
    bd = "3",
    command = openSettings
)
# Display the settings button
settingsButton.place(x = 853, y = 151)

# Create a function that opens the multiplayer window
def Multiplayer():
    os.system("python3 multiplayer.py")

# Create a button that opens the multiplayer window
multiplayerButton = tk.Button(
    text = "MULTIPLAYER",
    font = "Arial 11 bold",
    width = 15,
    height = 4,
    bg = "green",
    fg = "white",
    bd = "3",
    command = Multiplayer
)
multiplayerButton.place(x = 853, y = 239)

def News():
    os.system("python3 news.py")

newsButton = tk.Button(
    text = "NEWS",
    font = "Arial 11 bold",
    width = 15,
    height = 4,
    bg = "green",
    fg = "white",
    bd = "3",
    command = News
)
newsButton.place(x = 853, y = 63)

def Website():
    os.system("start website/site.html")
    
webButton = tk.Button(
    text = "WEBSITE",
    font = "Arial 11 bold",
    width = 15,
    height = 4,
    bg = "green",
    fg = "white",
    bd = "3",
    command = Website
)
webButton.place(x = 853, y = 327)

selectedVersion = "python3 versions/1.0/game.py"

def playVersion():
    os.system(selectedVersion)

playButton = tk.Button(
    text = "PLAY",
    font = "Arial 11 bold",
    width = 1000,
    height = 3,
    bg = "green",
    fg = "white",
    bd = "5",
    command = playVersion
)
playButton.pack(side = "bottom")

# Display player name
playerGreeting = tk.Label(
text = """
Welcome """ + settingsData.playerName + """
""",
font = "Arial 12 bold",
width = 1000,
bg = "gray30",
fg = "white")
playerGreeting.pack(side = "bottom")

window.mainloop()
