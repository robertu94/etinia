class DoubleDictionary:
    """dictionary with multiple keys for each value that will keep data syncronized"""
    def __init__(self):
        """Creates an empty dictionary"""
        self.ddict = {}
    def insert(self, k1, k2, v):
        """Inserts an element into the hashtable using both of its keys"""
        self.ddict[k1] = [k1,k2,v]
        self.ddict[k2] = [k1,k2,v]
    def exists(self, k):
        """Determines whether or not an element is in the hash table"""
        return self.ddict.get(k)
    def find(self, k):
        """Returns the value associated witht the key if it exists None otherwise"""
        if( (self.exists(k)) != None):
            return self.exists(k)[2]
        else:
            return None
    def remove(self, k):
        """Removes both references to the object in memory"""
        if(self.find(k)!= None):
            t = self.exists(k)
            del(self.ddict[t[0]])
            del(self.ddict[t[1]])
