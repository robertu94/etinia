class Character:
    img
    will
    strength
    defense
    speed
    exp
    gold
    skill # list of skills
    abilities # list of abilities
    equipment # list of equipment
 
    # default constructor
    def __init__(self):
        self.will = 6
        self.strenght = 0
        self.defense = 0
        self.speed = 0
        self.img = "@"
    # manual constructor
    def __init__(self, a, b, c, d, e):
       self.will = a
       self.strength = b
       self.defense = c
       self.speed = d
       self.img = e
    '''
       TODO
       Create method to import and construct the skill classes
       Create method to import and construct the equipment classes
       Create method to import and construct the abilites list
       Create methods to modify the skill list
       Create methods to modify the equipment list
       Create method to serialize the file
       Create method to deserialize the file
 
    '''

        

