from tkinter import *
import time

root = Tk()

canvas = Canvas(root, width='600', height='600')
canvas.pack()

def draw_fractal(x,y,size):
    time.sleep(0.01)
    canvas.update()
    if size < 10:
        return
    else:
        canvas.create_line(x,y,x+size,y, fill="black")
        canvas.create_line(x,y,x+size/2,y+size, fill="black")
        canvas.create_line(x+size,y,x+size/2,y+size, fill="black")

        draw_fractal(x,y,size/2)
        draw_fractal(x+size/2,y,size/2)
        draw_fractal(x+size/4,y+size/2,size/2)


draw_fractal(0,0,600)
root.mainloop()