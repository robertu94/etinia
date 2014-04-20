class Tile:
    # attributes
    def __init__(self, img = '.', effect = "", walkable=True):
        """Create a class that tracks the state of the tile"""
        self.img = img
        self.effect = effect
        self.walkable = walkable
    @staticmethod
    def load( a):
        datafile =  open("tile.dat", "r", encoding='utf-8')
        n = int(datafile.readline())
        s = ""
        for i in range(n):
            s = datafile.readline()
            if (s[0] == a):
                return Tile(s[0],s[1]=="T", s[2:])
        return Tile()
        
