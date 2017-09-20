from tkinter import *
import random
root = Tk()

window_width = 300
window_height = 300

canvas = Canvas(root, width = window_width, height = window_height)
canvas.pack()

# draw four different size and color rectangles.
colors = ["red", "green", "black", "blue", "yellow"]

X = input("Write Xvalue: ")
Y = input("Write Yvalue: ")

def draw_line_to_the_center(Xvalue, Yvalue):
    for i in range(4):
        random_number = random.randint(0,10)
        teal_line = canvas.create_rectangle(Xvalue+random_number*20, Yvalue+random_number*40, Xvalue+random_number*10, Yvalue+random_number*25, fill=random.choice(colors))


draw_line_to_the_center(int(X),int(Y))
root.mainloop()