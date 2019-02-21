class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.buf = [0] * 8
        self.size = 0

    def find_slot(self, buf, a):
        index = a % len(buf)
        while self.is_occupied(buf, index) and buf[index] != a:
            index = (index + 1) % len(buf)
        return index

    def is_occupied(self, buf, index):
        return buf[index] != 0 and buf[index] != float("inf")

    def lookup(self, buf, key):
        i = self.find_slot(buf, key)
        if self.is_occupied(buf, i):
            return True
        return False

    def set(self, buf, key, sz):
        i = self.find_slot(buf, key)
        if self.is_occupied(buf, i):
            return
        if sz + 1 == len(buf) - 2:
            new_buf = [0] * (2 * len(buf))
            new_sz = 0
            for a in buf:
                self.set(new_buf, a, new_sz)
                new_sz += 1
                i = self.find_slot(new_buf, key)
            new_buf[i] = key
            return new_buf
        buf[i] = key
        return buf

    def remove(self, buf, key):
        i = self.find_slot(buf, key)
        if not self.is_occupied(buf, i):
            return
        j = i
        while True:
            buf[i] = float("inf")
            while True:
                j = (j + 1) % len(buf)
                if not self.is_occupied(buf, j):
                    return
                k = buf[j] % len(buf)




    def resize(self, n):
        new_buf = [0] * n
        for i in range(min(self.size, n)):
            if i < self.size:
                new_buf[i] = self.buf[i]
        self.buf = new_buf

    def insert(self, val: 'int') -> 'bool':
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """

    def remove(self, val: 'int') -> 'bool':
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """

    def getRandom(self) -> 'int':
        """
        Get a random element from the set.
        """
