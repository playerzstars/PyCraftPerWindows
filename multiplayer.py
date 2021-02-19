# PyCraft Multiplayer Integration by ZachTheCoder

# PyCraft Launcher by ZachTheCoder

# Import libraries
import tkinter as tk
from PIL import ImageTk, Image
import socket
import os

# Set up the window
multiplayerWindow = tk.Tk()
multiplayerWindow.title("PyCraft Launcher")
multiplayerWindow.iconbitmap("assets/icon.ico")
multiplayerWindow.geometry("1000x900")
multiplayerWindow.resizable(0,0)
multiplayerWindow.configure(bg = "gray30")

# Create a title on the window
title = tk.Label(
    text = """
    Join a multiplayer game
    """,
    font = "Arial 13 bold",
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

# Create an input for the address of a multiplayer game
addressLabel = tk.Label(
    text = "Enter address",
    font = "Arial 13 bold",
    bg = "seashell4",
    fg = "white",
    width = 1000)
addressLabel.pack()

addressEntry = tk.Entry(
    width = 1000,
    font = "Arial 12",
    fg = "black")
addressEntry.pack()

def joinGame():
    quit()

playButton = tk.Button(
    text = "JOIN",
    font = "Arial 11 bold",
    width = 1000,
    height = 3,
    bg = "green",
    fg = "white",
    bd = "5",
    command = joinGame
)
playButton.pack(side = "bottom")

multiplayerWindow.mainloop()
