from map import Map
from character import Character
from rndgen import RndGen

class MapController:
    # active_unit TODO choose and change character to be moved
    def __init__(self, level):
        self.level = level  # map to control
        self.turn_order = []
        self.rnd = RndGen()

    #def set_active_unit(self, active_unit):
        #self.active_unit = active_unit

    def move(self, direction):
        if direction == "Left":
            if self.valid_move(self.level.units[0].x - 1, self.level.units[0].y, self.level.units[0]):
                self.level.units[0].move(self.level.units[0].x - 1, self.level.units[0].y)
        if direction == "Right":
            if self.valid_move(self.level.units[0].x + 1, self.level.units[0].y, self.level.units[0]):
                self.level.units[0].move(self.level.units[0].x + 1, self.level.units[0].y)
        if direction == "Up":
            if self.valid_move(self.level.units[0].x, self.level.units[0].y - 1, self.level.units[0]):
                self.level.units[0].move(self.level.units[0].x, self.level.units[0].y - 1)
        if direction == "Down":
            if self.valid_move(self.level.units[0].x, self.level.units[0].y + 1, self.level.units[0]):
                self.level.units[0].move(self.level.units[0].x, self.level.units[0].y + 1)


    def valid_move(self, x, y, mover):
        """Returns if the attempted move is a valid move"""
        if not (0 <= x < self.level.width and 0 <= y < self.level.height):
            return False 
        if not self.level.grid[y][x].walkable:
            return False
        for unit in self.level.units:
            if unit.x == x and unit.y == y and unit != mover:
                return False
        return True

    def recompute(self):
        for unit in self.level.units:
            self.turn_order.append( unit)
        self.turn_order.sort(reverse=True,key=lambda unit : unit.compute_init(self.rnd.draw()))

