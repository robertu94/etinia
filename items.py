class Item:
    def __init__(self, name = "Test", disc ="does stuff" effect = "even more"):
        """Creates the item class that will be inherited for weapons other other specialized item types"""
		self.name = name
        self.disc = disc
        self.effect = effect
    '''
    TODO
    Create item sack class to hold items
	Create a serialize method
	Create a deserialize method

    '''
