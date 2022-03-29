from tkinter import *

class window():
    def __init__(self, window_x, window_y):
        self.root = Tk()
        self.root.title("labyrinth visualiser")
        self.root.geometry(f"{window_x}x{window_y}")

        self.my_canvas = Canvas(self.root, width=window_x, height=window_y, bg="grey")
        self.my_canvas.pack()
        self.my_canvas.bind("<Button-1>", self.switch_state)
        self.my_canvas.focus_set()
        self.my_canvas.bind("<p>", self.printmap)
        self.my_canvas.bind("<b>", self.map_black)
        self.my_canvas.bind("<w>", self.map_white)
        self.my_canvas.bind("<g>", self.gradiant)
        self.my_canvas.bind("<q>", self.quit)
        return self.root

    def draw_rectangle(self, x: int, y: int, color:str):
        self.my_canvas.create_rectangle(x * self.pixel_size,
        y * self.pixel_size, (x + 1) * self.pixel_size,
        (y + 1) * self.pixel_size, fill=color)

    def draw_map(self, map):
        for y in range(len(map)):
            for x in range(len(map[y])):
                if map[y][x] == "X":
                    self.draw_rectangle(x, y, "black")
                elif map[y][x] == "o":
                    self.draw_rectangle(x, y, "red")
                else:
                    self.draw_rectangle(x, y, "white")

    def quit(self, event):
        self.my_canvas.quit()

    def switch_state(self, event):
        x = event.x // self.pixel_size
        y = event.y // self.pixel_size
        if self.map[y][x] == "X":
            self.draw_rectangle(x, y, "white")
            self.map[y][x] = '*'
        else:
            self.draw_rectangle(x, y, "black")
            self.map[y][x] = 'X'

    def printmap(self, event):
        for line in self.map:
            print("".join(line), end="\n")

    def map_black(self, event):
        self.set_map("X", "black")

    def map_white(self, event):
        self.set_map("*", "white")

    def gradiant(self, event):
        for y in range(len(self.map)):
            for x in range(len(self.map[y])):
                if self.map[y][x] == "*":
                    self.draw_rectangle(x, y,
                    rgb_to_hex((int((x+y) / (self.x + self.y) * 255),
                    int((1 - (x+y) / (self.x + self.y)) * 255), 255)))

def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb
