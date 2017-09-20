from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/line-play/r1.png]

def lines_drawer():
    for i in range(10,291,10):
        teal_line = canvas.create_line(i, 0, 300, i, fill='red')
        teal_line = canvas.create_line(0, i, i, 300, fill='green')

lines_drawer()

root.mainloop()


