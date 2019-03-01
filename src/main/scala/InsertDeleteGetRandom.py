import random

class RandomizedSet:
    def __init__(self):
        self.locs = {}
        self.nums = []

    def insert(self, val: 'int') -> 'bool':
        if val in self.locs:
            return False
        self.locs[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: 'int') -> 'bool':
        if not (val in self.locs):
            return False
        loc = self.locs[val]
        if loc < len(self.nums) - 1:
            self.nums[loc] = self.nums[len(self.nums) - 1]
            self.locs[self.nums[loc]] = loc
        del self.locs[val]
        self.nums.pop(len(self.nums) - 1)
        return True

    def getRandom(self) -> 'int':
        pos = random.randint(0, len(self.nums) - 1)
        return self.nums[pos]

randomSet = RandomizedSet()
randomSet.insert(1)
randomSet.remove(2)


randomSet.remove(0)
randomSet.remove(0)
randomSet.insert(0)
print(randomSet.getRandom())
randomSet.remove(0)
randomSet.insert(0)


