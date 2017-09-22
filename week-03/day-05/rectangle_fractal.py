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
        canvas.create_rectangle(x+size/3, y+size/3, x+size/3*2, y+size/3*2, fill="white")

        draw_fractal(x,y,size/3)
        draw_fractal(x+size/3, y, size/3)
        draw_fractal(x+size/3*2, y, size/3)

        draw_fractal(x, y+size/3, size/3)
        draw_fractal(x+size/3*2, y+size/3, size/3)

        draw_fractal(x, y+size/3*2, size/3)
        draw_fractal(x+size/3, y+size/3*2, size/3)
        draw_fractal(x+size/3*2, y+size/3*2, size/3)

blue_box = canvas.create_rectangle(0, 0, 600, 600, fill="dark blue")
draw_fractal(0,0,600)
root.mainloop()