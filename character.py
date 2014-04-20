class Character:
    def __init__(self,idval, x=0, y=0, will=6, strength=0, defense=0, speed=0, img="@", gold=0, exp=0,team = 0):
        """Create the base character Class"""
        self.idval = idval
        self.x = x
        self.y = y
        self.img = img
        self.will = will
        self.strength = strength
        self.defense = defense
        self.speed = speed
        self.exp = exp
        self.gold = gold
        self.team = team
        self.skill = [0]  # list of skills to be expanded once the skills class is created using int for now
        self.abilities = [0]  # list of abilities to be expanded once the abilities class is created using int for now
        self.equipment = [0]  # list of equipment to be expanded once the item class is created using int for now
        self.items = [0]  # list of non-equipped items to be expanded once the item class is finished

    @staticmethod
    def load(savefile):
        """Takes in a line from the save file that contians the information about the character
           Format:  x y will strength defense speed exp gold skills equipment
        """
        pass

    def __str__(self):
        """Converts the character to a string for easy saving"""
        savefile = ""
        savefile += self.img + " "
        savefile += (str(self.idval)) + ""
        savefile += (str(self.x)) + " "
        savefile += (str(self.y)) + " "
        savefile += (str(self.will)) + " "
        savefile += (str(self.strength)) + " "
        savefile += (str(self.defense)) + " "
        savefile += (str(self.speed)) + " "
        savefile += (str(self.exp)) + " "
        savefile += (str(self.team)) + " "
        savefile += (str(self.gold)) + " "
        savefile += (str(self.skill)) + " "
        return savefile

    def move(self, x, y):
        """Update the characters position"""
        self.x = x
        self.y = y
    def compute_init(rnd):
        return rnd + self.speed
    """
    TODO
    Create method to import and construct the skill classes
    Create method to import and construct the equipment classes
    Create method to import and construct the abilities list
    Create methods to modify the skill list
    Create methods to modify the equipment list
    Create method to serialize the file
    Create method to deserialize the file
    Create method to level up the hero to spend skill points
    """
