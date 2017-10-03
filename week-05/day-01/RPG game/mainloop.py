from tkinter import *
from class_entity import *

root = Tk()

image_01 = PhotoImage(file = "image/floor.png")
image_02 = PhotoImage(file = "image/wall.png")
hero_down = PhotoImage(file = "image/hero-down.png")
hero_up = PhotoImage(file = "image/hero-up.png")
hero_right = PhotoImage(file = "image/hero-right.png")
hero_left = PhotoImage(file = "image/hero-left.png")
map_name = "map.txt"
canvas = Canvas(root, width = 700, height = 770, bg = "white")
canvas.pack()

def import_walls_to_list(file_name):
    try:
        with open(file_name, "r") as f:
            line_list = f.read().splitlines()
            return draw_tiles(line_list)
    except Exception:
        print("File read error!")


def draw_tiles(wall_list):
    distance = 70
    for i, line in enumerate(wall_list):
        for j, value in enumerate(line):
            if str(value) == "0":
                image_floor = canvas.create_image(35+j*distance, 35+i*distance, image = image_01)
            elif str(value) == "1":
                image_floor = canvas.create_image(35+j*distance, 35+i*distance, image = image_02)


def draw_hero(hero_image):
    hero_char = canvas.create_image(hero.X, hero.Y, image = hero_image)
    

def move_hero(hero, dx, dy):
    canvas.move(hero_char , dx, dy)



def on_key_press(e):
    if ( e.keysym == 'Up' ):
        draw_hero(hero_up)
        move_hero(0,-70)
    elif( e.keysym == 'Down' ):
        draw_hero(hero_down)
        move_hero(0,70)
    elif( e.keysym == 'Right'):
        draw_hero(hero_right)
        move_hero(70,0)
    elif( e.keysym == 'Left'):
        draw_hero(hero_left)
        move_hero(-70,0)

import_walls_to_list(map_name)
hero = Hero()
draw_hero(hero_down)
root.bind("<KeyPress>", on_key_press)
root.mainloop()