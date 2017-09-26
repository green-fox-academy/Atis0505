from tkinter import *
import time

root = Tk()

canvas = Canvas(root, width='600', height='600')
canvas.pack()
width=30
counter = 0
def draw_lines(x,y,size):
    time.sleep(0.001)
    canvas.update()
    if size <= 50:
        return 0
    else:
        canvas.create_polygon([x+size/4,y+size/2-0.866*size/2, x+size/4*3,y+size/2-0.866*size/2, x+size,y+size/2, x+size/4*3,y+size/2+0.866*size/2, x+size/4,y+size/2+0.866*size/2, x, y+size/2],outline='black', fill='', width=2)

        draw_lines(x+size/4,y+size/2-0.866*size/2,size/3)
        draw_lines(x+size/4+size/2,y+size/2-0.866*size/2,size/3)
        

lime_box = canvas.create_rectangle(0,0,600,600, fill="yellow")
draw_lines(0,0,600)
root.mainloop()