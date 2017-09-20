from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# draw 3 lines with that function.
X = input("Write Xvalue: ")
Y = input("Write Yvalue: ")

def draw_line_to_the_center(Xvalue, Yvalue):
    teal_line = canvas.create_line(Xvalue, Yvalue, 150, 150, fill='dark blue')


draw_line_to_the_center(int(X),int(Y))
root.mainloop()