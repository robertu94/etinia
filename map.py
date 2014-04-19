from tile import Tile
from character import Character


class Map:

    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.grid = [[Tile() for x in range(width)] for x in range(height)]
        self.units = []

    @staticmethod
    def load(filename):
        """Returns a map for the given data file."""
        file = open(filename, "r", encoding='utf-8')
        height = int(file.readline())
        width = int(file.readline())
        temp_map = Map(height, width)
        for row in range(0, height):
            row_string = file.readline()
            for j in range(0, width):
                temp_map.grid[row][j] = Tile(row_string[j])
        return temp_map

    def __str__(self):
        char_grid = []  # 2d array of char
        for row in range(0, self.height):
            char_row = [None] * self.width
            for j in range(0, self.width):
                char_row[j] = self.grid[row][j].img
            char_grid.append(char_row)
        print(self.units)
        for unit in self.units:
            char_grid[unit.y][unit.x] = unit.img
        string = ""
        for row in char_grid:
            string += "".join(row)
            string += "\n"
        return string

    def add_unit(self, unit):
        """Add a character to the map"""
        self.units.append(unit)
