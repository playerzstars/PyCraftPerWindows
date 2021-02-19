# Import libraries
import tkinter as tk
import os

# Import settings data
import settingsData

# Set up the window
settingsWindow = tk.Tk()
settingsWindow.title("PyCraft Launcher")
settingsWindow.iconbitmap("assets/icon.ico")
settingsWindow.geometry("1000x900")
settingsWindow.resizable(0,0)
settingsWindow.configure(bg = "gray30")

# Create a title on the window
title = tk.Label(
    text = """
    PyCraft Launcher Settings
    """,
    font = "Arial 12 bold",
    width = 1000,
    bg = "seashell4",
    fg = "white")
title.pack()

# Blank space
blankSpace = tk.Label(bg = "gray30")
blankSpace.pack()

# Blank space
blankSpace = tk.Label(bg = "gray30")
blankSpace.pack()

# Blank space
blankSpace = tk.Label(bg = "gray30")
blankSpace.pack()

# Display the current player name
selectedPlayerName = tk.Label(
    text = "Name:   " + settingsData.playerName,
    font = "Arial 12 bold",
    width = 1000,
    height = 2,
    bg = "seashell4",
    fg = "white"
    )
selectedPlayerName.pack()

# Create a function that allows the user the change the player name
def changeName():
    os.system("python3 changeName.py")

# Create a button that allows the user to change the player name
changeNameButton = tk.Button(
    text = "CHANGE",
    font = "Arial 11 bold",
    width = 15,
    height = 2,
    bg = "green",
    fg = "white",
    bd = "3",
    command = changeName
)
changeNameButton.place(x = 853, y = 123)

# Keep the window open
settingsWindow.mainloop()
