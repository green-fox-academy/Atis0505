from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# draw the canvas' diagonals in green.
teal_line = canvas.create_line(0, 0, 300, 300, fill='dark blue')

root.mainloop()