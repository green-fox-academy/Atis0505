from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/purple-steps/r3.png]

def sqaure_drawing():
    
    moving_size = 0;
    for i in range(15):
        teal_line = canvas.create_rectangle(0+moving_size,0+moving_size,20+moving_size,20+moving_size, fill="purple")
        moving_size += 20


sqaure_drawing()
root.mainloop()