from tile import Tile
class TileFactory:
    """Class staticly creates the appropriate tile from the database in tile.dat"""
    def __init__(self):
        datafile =  open("tile.dat", "r", encoding='utf-8')
        self.factory= {}
        n = int(datafile.readline())
        s = ""
        for i in range(n):
            s = datafile.readline()
            self.factory[s[0]] = Tile(s[0],s[1]=="T", s[2:])
    def load(self, a):
        if (self.factory.get(a) == None):
            return Tile()
        else:
            return self.factory[a]
