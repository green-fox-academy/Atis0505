from tkinter import *

root = Tk()
window_width = 300
window_height = 300
# draw a green 10x10 square to the center of the canvas.
canvas = Canvas(root, width = window_width, height = window_height)
canvas.pack()

size_number = int(input("Size of the square: "))

def draw_square_in_middle(size_value):
    lime_box = canvas.create_rectangle(window_width/2-size_number/2, window_height/2-size_number/2, window_width/2+size_number/2, window_height/2+size_number/2, fill='lime green')


draw_square_in_middle(size_number)
root.mainloop()