import random

class RandomizedSet:
    
    def __init__(self):
        self.lst = []
        self.index = {}
        
    def search(self, val):
        return val in self.index
    
    def insert(self, val: int) -> bool:
        if self.search(val):
            return False
        
        self.lst.append(val)
        self.index[val] = len(self.lst) - 1
        return True
    
    def remove(self, val: int) -> bool:
        if not self.search(val):
            return False
        
        idx = self.index[val]
        self.lst[idx] = self.lst[-1]
        self.index[self.lst[-1]] = idx
        self.lst.pop()
        del self.index[val]
        return True
    
    def getRandom(self) -> int:
        return random.choice(self.lst)