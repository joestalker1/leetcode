import random

class RandomizedSet:
    def __init__(self):
        self.num_to_pos = {}
        self.nums = []

    def insert(self, val: 'int') -> 'bool':
        if val in self.num_to_pos:
            return False
        self.nums.append(val)
        self.num_to_pos[val] = len(self.nums) - 1
        return True

    def remove(self, val: 'int') -> 'bool':
        if val not in self.num_to_pos:
            return False
        # move num to the end of nums to pop it up
        a = self.nums[-1]
        i = self.num_to_pos[val]
        self.num_to_pos[a] = i
        self.nums[i] = a
        self.nums.pop()
        del self.num_to_pos[val]
        return True

    def getRandom(self) -> 'int':
        return self.nums[random.randint(0, len(self.nums) - 1)]
