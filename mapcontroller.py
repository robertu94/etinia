from map import Map
from character import Character


class MapController:
    # active_unit TODO choose and change character to be moved
    def __init__(self, level):
        self.level = level  # map to control
        
    #def set_active_unit(self, active_unit):
        #self.active_unit = active_unit

    def move(self, direction):
        if direction == "Left":
            if self.level.valid_move(self.level.units[0].x - 1, self.level.units[0].y, self.level.units[0]):
                self.level.units[0].move(self.level.units[0].x - 1, self.level.units[0].y)
        if direction == "Right":
            if self.level.valid_move(self.level.units[0].x + 1, self.level.units[0].y, self.level.units[0]):
                self.level.units[0].move(self.level.units[0].x + 1, self.level.units[0].y)
        if direction == "Up":
            if self.level.valid_move(self.level.units[0].x, self.level.units[0].y - 1, self.level.units[0]):
                self.level.units[0].move(self.level.units[0].x, self.level.units[0].y - 1)
        if direction == "Down":
            if self.level.valid_move(self.level.units[0].x, self.level.units[0].y + 1, self.level.units[0]):
                self.level.units[0].move(self.level.units[0].x, self.level.units[0].y + 1)
