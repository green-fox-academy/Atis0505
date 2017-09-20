from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/purple-steps/r3.png]

def sqaure_drawing():
    x = 0
    y = 0
    size = 10
    for i in range(1,7):
        x_v = x + size
        y_v = y + size
        teal_line = canvas.create_rectangle(x, y, x_v, y_v, fill="purple")
        size += 10
        x = x_v
        y = y_v

sqaure_drawing()
root.mainloop()