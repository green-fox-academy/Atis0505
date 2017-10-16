from tkinter import *
# from entity_class import *

root = Tk()

image_01 = PhotoImage(file = "image/floor.png")
image_02 = PhotoImage(file = "image/wall.png")
hero_down = PhotoImage(file = "image/hero-down.png")
hero_up = PhotoImage(file = "image/hero-up.png")
hero_right = PhotoImage(file = "image/hero-right.png")
hero_left = PhotoImage(file = "image/hero-left.png")
map_name = "map.txt"
distance = 70
canvas = Canvas(root, width = 700, height = 770, bg = "white")
canvas.pack()


def import_walls_to_list(file_name):
    try:
        with open(file_name, "r") as f:
            line_list = f.read().splitlines()
            return line_list
    except Exception:
        print("File read error!")


def draw_and_check_tiles():
    wall_list = import_walls_to_list(map_name)
    for i, line in enumerate(wall_list, start = 0):
        for j, value in enumerate(line, start = 0):
            if i > 0 and i < len(wall_list) and j > 0 and j < len(line):
                if str(value) == "0":
                    image_floor = canvas.create_image(35+(j-1)*distance, 35+(i-1)*distance, image = image_01)
                elif str(value) == "1":
                    image_floor = canvas.create_image(35+(j-1)*distance, 35+(i-1)*distance, image = image_02)


def check_next_tile(x, y):
    wall_list = import_walls_to_list(map_name)
    for i, line in enumerate(wall_list, start = 0):
        for j, value in enumerate(line, start = 0):
            if i > 0 and i < len(wall_list) and j > 0 and j < len(line):
                if str(value) == "0":
                    if y == (35+(i-1)*distance) and x == (35+(j-1)*distance):
                        return True
                elif str(value) == "1":
                    if y == (35+(i-1)*distance) and x == (35+(j-1)*distance):
                        return False
                    

class Entity:
    def __init__(self, entity_type):
        self.health_point = 0
        self.attack_damage = 0
        self.entity_type = entity_type
        if entity_type == "hero":
            self.X = 35
            self.Y = 35


    def move(self, dx,dy):
        self.X += dx
        self.Y += dy
        canvas.move(self.draw_char_image, dx, dy)

    
    def draw_char_image(self, entity_image):
        self.draw_char_image = canvas.create_image(self.X, self.Y, image = entity_image)

    
    def update_costume(self, entity_image):
        canvas.itemconfigure(self.draw_char_image, image = entity_image)


def on_key_press(e):
    if ( e.keysym == 'Up' ):
        if check_next_tile(hero.X, hero.Y-distance) == True:
            hero.move(0,-distance)
            hero.update_costume(hero_up)
        else:
            hero.move(0,0)
            hero.update_costume(hero_up)
        
    elif( e.keysym == 'Down' ):
        if check_next_tile(hero.X, hero.Y+distance) == True:
            hero.move(0,distance)
            hero.update_costume(hero_down)
        else:
            hero.move(0,0)
            hero.update_costume(hero_down)
    elif( e.keysym == 'Right'):
        if check_next_tile(hero.X+distance, hero.Y) == True:
            hero.move(distance,0)
            hero.update_costume(hero_right)
        else:
            hero.move(0,0)
            hero.update_costume(hero_right)
    elif ( e.keysym == 'Left'):
        if check_next_tile(hero.X-distance, hero.Y) == True:
            hero.move(-distance,0)
            hero.update_costume(hero_left)
        else:
            hero.move(0,0)
            hero.update_costume(hero_left)
    


draw_and_check_tiles()
hero = Entity("hero")
hero.draw_char_image(hero_down)    
root.bind("<KeyPress>", on_key_press)


root.mainloop()