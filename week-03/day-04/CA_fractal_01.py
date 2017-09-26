from tkinter import *
import time

root = Tk()

canvas = Canvas(root, width='600', height='600')
canvas.pack()

counter = 0
def draw_lines(a,x, y):
    time.sleep(0.1)
    canvas.update()
    if a <= 5:
        return 0
    else:
        teal_line = canvas.create_line(x+a/3, y, x+a/3, y+a, fill="black")
        teal_line = canvas.create_line(x+a/3*2, y, x+a/3*2, y+a, fill="black")
        teal_line = canvas.create_line(x, y+a/3, x+a, y+a/3, fill="black")
        teal_line = canvas.create_line(x, y+a/3*2, x+a, y+a/3*2, fill="Black")
        return draw_lines(a/3, x+a/3, y), draw_lines(a/3, x, y+a/3), draw_lines(a/3, x+a/3*2,  y+a/3), draw_lines(a/3, x+a/3, y+a/3*2)

lime_box = canvas.create_rectangle(0,0,600,600, fill="yellow")
teal_line = canvas.create_line(0, 0, 600, 0, fill="black")
teal_line = canvas.create_line(0, 0, 600, 0, fill="black")
teal_line = canvas.create_line(0, 600, 600, 600, fill="black")
teal_line = canvas.create_line(600, 0, 600, 600, fill="black")
draw_lines(600,0,0)
root.mainloop()

    
    