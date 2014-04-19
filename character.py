class Character:
    # default constructor
    # manual constructor
    def __init__(self, x=0, y=0, will=6, strength=0, defense=0, speed=0, img="@", gold=0, exp=0):
        """Create the base character Class"""
        self.x = x
        self.y = y
        self.img = img
        self.will = will
        self.strength = strength
        self.defense = defense
        self.speed = speed
        self.exp = exp
        self.gold = gold
        self.skill = [0]  # list of skills to be expanded once the skills class is created using int for now
        self.abilities = [0]  # list of abilities to be expanded once the abilities class is created using int for now
        self.equipment = [0]  # list of equipment to be expanded once the item class is created using int for now
        self.items = [0]  # list of non-equipped items to be expanded once the item class is finished

    '''
       TODO
       Create method to import and construct the skill classes
       Create method to import and construct the equipment classes
       Create method to import and construct the abilities list
       Create methods to modify the skill list
       Create methods to modify the equipment list
       Create method to serialize the file
       Create method to deserialize the file
       Create method to level up the hero to spend skill points
    '''

        

