import math
from collections import defaultdict

class MRUQueue:

    def __init__(self, n: int):
        self.n = n
        self.sz = int(math.sqrt(n))
        self.blocks = defaultdict(list)
        for i in range(1, n + 1):
            self.blocks[(i - 1) // self.sz].append(i)

    def fetch(self, k):
        block_num = (k - 1) // self.sz
        #position inside block
        j = (k-1) % self.sz
        res = self.blocks[block_num][j]
        self.blocks[block_num].pop(j)
        last = (self.n-1) // self.sz
        self.blocks[last].append(res)
        # shift blocks
        for i in range(last, block_num, -1):
            x = self.blocks[i].pop(0)
            self.blocks[i - 1].append(x)
        return res

q = MRUQueue(8)
print(q.fetch(3))#3
print(q.fetch(5))#6
print(q.fetch(2))#2
print(q.fetch(8))#2



