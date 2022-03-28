#!/usr/bin/env python3

import sys
from visualiser import window

class map(window):
    def __init__(self) -> None:
        self.x = 0
        self.y = 0
        self.pixel_size = 10
        self.map = []
        if not self.getargs():
            return
        self.window = super().__init__(self.x * self.pixel_size, self.y * self.pixel_size)
        super().draw_map(self.map)
        self.window.mainloop()

    def getargs(self):
        if len(sys.argv) == 3:
            self.x = int(sys.argv[1])
            self.y = int(sys.argv[2])
            self.create_map_size()
        elif len(sys.argv) == 2:
            self.map_path = sys.argv[1]
            self.create_map_from_file()
        else:
            print(f"{sys.argv[0]} [x | file_name] (y)")
            return False
        self.pixel_size = (1000 // self.y) if (1080 // self.y < 1920 // self.x) else (1920 // self.x)
        return True

    def set_map(self, char, color):
        for y in range(len(self.map)):
            for x in range(len(self.map[y])):
                self.draw_rectangle(x, y, color)
                self.map[y][x] = char

    def create_map_from_file(self):
        nb_line = 0
        with open(self.map_path, "r") as file:
            for line in file:
                if (line.startswith("\n")):
                    break
                self.map.append([])
                for column in line:
                    if column != "\n":
                        self.map[nb_line].append(column)
                nb_line += 1
            self.x = len(self.map[0])
        self.y = nb_line
        if 1080 // self.y < 1920 // self.x:
            self.pixel_size = 1000 // self.y
        else:
            self.pixel_size = 1920 // self.x

    def create_map_size(self):
        for line in range(self.y):
            self.map.append([])
            for column in range(self.x):
                self.map[line].append('*')

if __name__ == '__main__':
    map()
