import math

class MaxSegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [-math.inf] * (2 * (self.n + 1))
        self.construct(arr)

    def get_max(self, lo, hi):
        lo += self.n
        hi += self.n
        maxs = -math.inf
        while lo <= hi:
            if lo % 2 == 1:
                maxs = max(maxs, self.tree[lo])
                lo += 1
            if hi % 2 == 0:
                maxs = max(maxs, self.tree[hi])
                hi -= 1
            lo = lo // 2
            hi = hi // 2
        return maxs

    def update(self, i, x):
        #get leave index
        i += self.n
        self.tree[i] = x
        #parent index
        i = i // 2
        while i >= 1:
            self.tree[i] = max(self.tree[2 * i], self.tree[2 * i + 1])
            i = i // 2

    def construct(self, arr):
        for i in range(len(arr)):
            self.update(i, arr[i])


seg_tree = MaxSegmentTree([1,2,3,1])
print(seg_tree.get_max(0,1)==2)
print(seg_tree.get_max(0,3)==3)
print(seg_tree.get_max(3,3)==1)
print(seg_tree.get_max(1,2)==3)

