class archetype():
    """
    a base class for all characters from which all character like classes will inherit
    """
    def __init__(self, idval, name, hand_limit= 2, armor_limit=3, gear_limit=0, hands =[], armor=[], gear=[], skill_limit = 5, skills=[], dna=3, strength = 0, speed = 0, defenses = 0 , will =6, subunit = []):

        #max size of the hand list
        self.hand_limit = hand_limit

        #max size of the armor list
        self.armor_limit = armor_limit

        #max size of the gear lsit
        self.gear_limit = gear_limit

        # list containing the characters hand items
        self.hands = hands

        # list containing the characters armor items
        self.armor = armor

        # list containing the characters gear items
        self.gear = gear

        # max size of the skill list
        self.skill_limit = skill_limit

        # list containing the players skills
        self.skills = skills

        # value that describes the maximum of several physical values
        self.dna = dna
        self.strength = strength
        self.speed = speed
        self.defenses = defenses
        self.will = will

        # list of units that make up this unit
        self.subunit = subunit

        # unique idvalue
        self.idval = idval
        self.name = name

        # contains a path to the file that should represent the character
        self.img = img


class player(archetype):
    """
    Representation of the player and player-like characters in the game
    """
    def __init__(self, idval, name, hand_limit= 2, armor_limit=3, gear_limit=0, hands =[], armor=[], gear=[], skill_limit = 5, skills=[], dna=3, strength = 0, speed = 0, defenses = 0 , will =6, subunit = [],exp = 0 , gold =0 , items= []):
        super(player, self).__init__(idval, name, hand_limit, armor_limit, gear_limit, hands , armor, gear, skill_limit , skills, dna, strength , speed , defenses , will , subunit)
        self.exp = exp
        self.gold = gold
        self.items = items
        
        
class Character:
    def __init__(self,idval, x=0, y=0, will=6, strength=0, defense=0, speed=0, img="@", gold=0, exp=0,team = 0):
        """Create the base character Class"""
        self.exp = exp
        self.gold = gold
        self.items = [0]  # list of non-equipped items to be expanded once the item class is finished

    def save(self):
        """
        Returns a serialized form of the character
        """
        pass

    def load(self):
        """
        Loads the character from serialized from
        """
        pass

    def move(self, x, y):
        """Update the characters position"""
        self.x = x
        self.y = y

    def compute_initiative(rnd):
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
