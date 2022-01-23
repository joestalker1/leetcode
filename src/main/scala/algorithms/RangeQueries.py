def rangeSum(arr, a, b):
    if not arr or a > b:
        return 0
    prefix_sum = [0] * len(arr)
    for i in range(0, len(prefix_sum)):
        if i == 0:
            prefix_sum[i] = arr[i]
        else:
            prefix_sum[i] = prefix_sum[i-1] + arr[i]

    return prefix_sum[b] - prefix_sum[a - 1]

def rangeMin(arr, a, b):
    if not arr or a > b:
        return 0
    return None


class FenwickTree:
    def __init__(self, arr):
        self.tree = [0] * (len(arr) + 1)
        self.construct(arr)

    def update(self, i, v):
        i += 1
        while i < len(self.tree):
            self.tree[i] += v
            i += i & (-i)

    def sum(self, i):
        s = 0
        i += 1

        while i > 0:
            s += self.tree[i]
            i -= i & (-i)
        return s

    def construct(self, arr):
        for i in range(len(arr)):
            self.update(i, arr[i])


class SegmentTree:
    def __init__(self, arr):
        self.tree = [0] * (2 * len(arr))
        self.n = len(arr)
        self.construct(arr)

    def sum(self, lo, hi):
        #get leave indexes
        lo += self.n
        hi += self.n
        s = 0
        while lo <= hi:
            if lo % 2 == 1:
                s += self.tree[lo]
                lo += 1
            if hi % 2 == 0:
                s += self.tree[hi]
                hi -= 1
            lo = lo // 2
            hi = hi // 2
        return s

    def update(self, i, x):
        i += self.n
        self.tree[i] += x
        i = i // 2
        while i >= 1:
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]
            i = i // 2

    def construct(self, arr):
        for i in range(len(arr)):
            self.update(i, arr[i])

class MinSegmentTree:
    def __init__(self, arr):
        self.tree = [0] * (2 * (len(arr)+1))
        self.n = len(arr)
        self.construct(arr)

    def min(self, lo, hi):
        lo += self.n
        hi += self.n
        mins = float("inf")
        while lo <= hi:
            if lo % 2 == 1:
                mins = min(mins, self.tree[lo])
                lo += 1
            if hi % 2 == 0:
                mins = min(mins, self.tree[hi])
                hi -= 1
            lo = lo // 2
            hi = hi // 2
        return mins

    def update(self, i, x):
        #get leave index
        i += self.n
        self.tree[i] = x
        #parent index
        i = i // 2
        while i >= 1:
            self.tree[i] = min(self.tree[2 * i], self.tree[2 * i + 1])
            i = i // 2

    def construct(self, arr):
        for i in range(len(arr)):
            self.update(i, arr[i])


arr = [1,3,4,8,6,1,4,2]
ftree = FenwickTree(arr)
s = ftree.sum(6) - ftree.sum(2)
print(s)
seg_tree = MinSegmentTree(arr)
print(seg_tree.min(6, 7))

print(rangeSum([1,3,4,8,6,1,4,2], 3, 6))