from math import log2,floor,inf

# max segment wit lazy increment
class SegmentTree:
    def __init__(self, arr):
        self.arr_len = len(arr)
        self.tree = [0] * (2 * self.arr_len)
        # lazy applying changes
        #update for every leave
        self.d = [inf] * self.arr_len
        self.h = floor(log2(self.arr_len)) + 1
        #fill up the leaves
        for i in range(self.arr_len):
            self.tree[i + self.arr_len] = arr[i]
        #fill up the inner nodes
        self.build(self.arr_len)

    def build(self, p):
        while p > 1:
            p >>= 1
            self.tree[p] = max(self.tree[p << 1], self.tree[p << 1 | 1]) + self.d[p]

    def push(self, p):
        s = self.h
        while s > 0:
            i = p >> s
            if self.d[i] != inf:
                self.apply(i << 1, self.d[i])
                self.apply(i << 1 | 1, self.d[i])
                self.d[i] = inf
            s -= 1

    def apply(self, p, val):
        self.tree[p] += val
        if p < self.arr_len:
            self.d[p] += val

    def inc(self, l, r, val):
        l += self.arr_len
        r += self.arr_len
        l0 = l
        r0 = r
        while l < r:
            if l & 1:
                self.apply(l, val)
                l += 1
            if r & 1:
                r -= 1
                self.apply(r, val)
            l >>= 1
            r >>= 1
        self.build(l0)
        self.build(r0-1)

    #sum of interval [l,r)
    def query(self, l, r):
        l += self.arr_len
        r += self.arr_len
        self.push(l)
        self.push(r - 1)
        res = -inf
        while l < r:
            if l & 1:
                res = max(res,self.tree[l])
                l += 1
            if r & 1:
                r -= 1
                res = max(res,self.tree[r])
            l >>= 1
            r >>= 1
        return res



arr = [8, 7, 3, 9, 5, 1, 10]

st = SegmentTree(arr)
print(st.query(1, 3))