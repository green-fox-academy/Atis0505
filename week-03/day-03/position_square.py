from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

x = 0
y = 0

# create a square drawing function that takes 2 parameters:
# the x and y coordinates of the square's top left corner
# and draws a 50x50 square from that point.
# draw 3 squares with that function.
def sqaure_drawing(xparam, yparam):
    moving_size = 0;
    for i in range(3):
        teal_line = canvas.create_rectangle(xparam+moving_size,yparam+moving_size,50+moving_size,50+moving_size, fill="orange")
        moving_size += 50


sqaure_drawing(int(x),int(y))
root.mainloop()