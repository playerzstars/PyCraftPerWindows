# PyCraft News by ZachTheCoder

# Import libraries
import tkinter as tk
from PIL import ImageTk, Image
import os

# Set up the window
newsWindow = tk.Tk()
newsWindow.title("PyCraft Launcher")
newsWindow.iconbitmap("assets/icon.ico")
newsWindow.geometry("1000x900")
newsWindow.resizable(0, 0)
newsWindow.configure(bg = "gray30")

# Create a title on the window
title = tk.Label(
    text = """
    PyCraft News
    """,
    font = "Arial 12 bold",
    width = 1000,
    bg = "seashell4",
    fg = "white")
title.pack()

# Create a back button
backButton = tk.Button(
    text = "BACK",
    font = "Arial 11 bold",
    width = 1000,
    height = 3,
    bg = "green",
    fg = "white",
    bd = "5",
    command = quit
)
backButton.pack()

# Blank space
blankSpace = tk.Label(bg = "gray30")
blankSpace.pack()

# Blank space
blankSpace = tk.Label(bg = "gray30")
blankSpace.pack()

# Blank space
blankSpace = tk.Label(bg = "gray30")
blankSpace.pack()

# Create a description for Alpha 1.0 on the window
alphaOnePointZeroDesc = tk.Label(
    text = """
Alpha 1.0
    
Very first version of PyCraft. Added Launcher and a simple program that generates a terrain of 20x20 white blocks and
allows the user to place and destroy blocks.
    """,
    font = "Arial 12 bold",
    width = 1000,
    bg = "seashell4",
    fg = "white")
alphaOnePointZeroDesc.pack()

newsWindow.mainloop()
