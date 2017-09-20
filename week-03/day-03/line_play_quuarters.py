from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# divide the canvas into 4 equal parts
# and repeat this pattern in each quarter:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/line-play/r1.png]

def lines_drawer(x,y,a,b,color):
    teal_line = canvas.create_line(x, y, a, b, fill=color)


i=0
while (i < 150):
    lines_drawer(0, 0+i, 0+i, 150, "red")
    lines_drawer(0+i,0,150,0+i, "green")

    lines_drawer(150, 0+i, 150+i, 150, "red")
    lines_drawer(150+i,0,300,0+i, "green")

    lines_drawer(0, 150+i, 0+i, 300, "red")
    lines_drawer(0+i,150,150,150+i, "green")

    lines_drawer(150, 150+i, 150+i, 300, "red")
    lines_drawer(150+i,150,300,150+i, "green")


    i+=10

root.mainloop()