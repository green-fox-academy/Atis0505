from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# fill the canvas with a checkerboard pattern.

def checkerboard_drawer(square_size):
    for i in range(0,int(300/square_size)):
        for j in range(0,int(300/square_size)):
            if (i%2==0 and j%2==0) or (i%2==1 and j%2==1):
                teal_line = canvas.create_rectangle(square_size*i, square_size*j, square_size*(i+1), square_size*(j+1), fill="black")


checkerboard_drawer(50)
root.mainloop()