class RandomizedSet:
    l= []
    def __init__(self):
        self.L = []

    def insert(self, val: int) -> bool:
        if val not in self.L:
            self.L.append(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val not in self.L:
            return False
        else:
            self.L.remove(val)
            return True

    def getRandom(self) -> int:
        return random.choice(self.L)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
