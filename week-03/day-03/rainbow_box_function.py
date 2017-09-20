from tkinter import *

root = Tk()
window_width = 500
window_height = 500

canvas = Canvas(root, width=window_width, height=window_height)
canvas.pack()

# create a square drawing function that takes 2 parameters:
# the square size, and the fill color,
# and draws a square of that size and color to the center of the canvas.
# create a loop that fills the canvas with rainbow colored squares.

colors = ["red", "light blue", "green", "black", "blue", "yellow", "dark blue" ]

def rainbow_drawer_with_squares(size):
    
    for color in colors:
        lime_box = canvas.create_rectangle(window_width/2-size/2, window_height/2-size/2, window_width/2+size/2, window_height/2+size/2, fill = color)
        size -= 30


rainbow_drawer_with_squares(window_width)
root.mainloop()