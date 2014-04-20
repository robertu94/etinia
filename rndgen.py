from random import shuffle
class RndGen:
    def __init__(self):
        """creates and suffles a deck"""
        self.deck = [-2,-2,-2,-2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,11,11,11,11,12,12,12,12,13,13,13,13,14,14,14,14,15,15]
        shuffle(self.deck)
    def reset(self):
        """returns the deck to its inital state"""
        self.deck = [-2,-2,-2,-2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,11,11,11,11,12,12,12,12,13,13,13,13,14,14,14,14,15,15]
        shuffle(self.deck)
    
    def is_empty(self):
        """returns true if the deck is empty"""
        return (len(self.deck) == 0)
    
    def draw(self):
        """returns the value of the card drawn and returns it to the deck"""
        if (self.is_empty()):
            self.reset()
            return self.draw()
        else:
            a = self.deck[len(self.deck)-1]
            del self.deck[len(self.deck)-1]
            return a
