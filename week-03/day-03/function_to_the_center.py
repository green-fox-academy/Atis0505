from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

X_from_user = 210
Y_from_user = 270

# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# fill the canvas with lines from the edges, every 20 px, to the center.
def lines_drawer(X_edge, Y_edge):     
            teal_line = canvas.create_line(X_edge, Y_edge, X_from_user, Y_from_user, fill='red')


i = 0
while(i <= 300):
    lines_drawer(0, i)
    lines_drawer(300, i)
    lines_drawer(i, 0)
    lines_drawer(i, 300)
    i += 20

root.mainloop()