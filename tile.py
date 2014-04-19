class Tile:
    # attributes
    def __init__(self, img = '.', effect = "", walkable=True):
        """Create a class that tracks the state of the tile"""
        self.img = img
        self.effect = effect
        self.walkable = walkable

