class RandomizedCollection:

    def __init__(self):
        self.val_to_pos = defaultdict(set)
        self.vals = []

    def insert(self, val: int) -> bool:
        self.val_to_pos[val].add(len(self.vals))
        self.vals.append(val)
        return len(self.val_to_pos[val]) == 1

    def remove(self, val: int) -> bool:
        if not self.val_to_pos[val]:
            return False
        i = self.val_to_pos[val].pop()
        last = self.vals[-1]
        self.vals[i] = last
        self.val_to_pos[last].add(i)
        self.val_to_pos[last].discard(len(self.vals) - 1)
        self.vals.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.vals)