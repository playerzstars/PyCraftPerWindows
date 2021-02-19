# Change Name by ZachTheCoder

# Import libraries
import tkinter as tk
import os

# Set up the window
changeNameWindow = tk.Tk()
changeNameWindow.title("Change name")
changeNameWindow.iconbitmap("assets/icon.ico")
changeNameWindow.geometry("1000x500")
changeNameWindow.resizable(0,0)
changeNameWindow.configure(bg = "gray30")

# Create a title on the window
title = tk.Label(
    text = """
    Change name
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

# In-game name selection
nameLabel = tk.Label(
    text = "Name",
    font = "Arial 13 bold",
    bg = "seashell4",
    fg = "white",
    width = 1000)
nameLabel.pack()

nameEntry = tk.Entry(
    width = 1000,
    font = "Arial 12",
    fg = "black")
nameEntry.pack()

# Create a function that saves the name
def saveName():
    data = open("settingsData.py", "w")
    data.write('playerName = "' + nameEntry.get() + '"')
    data.close()
    quit()

# Create a button that saves the name
saveNameButton = tk.Button(
    text = "SAVE",
    font = "Arial 11 bold",
    width = 1000,
    height = 3,
    bg = "green",
    fg = "white",
    bd = "3",
    command = saveName)

# Display the save button
saveNameButton.pack(side = "bottom")

changeNameWindow.mainloop()
