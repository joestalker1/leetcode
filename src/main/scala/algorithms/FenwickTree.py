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



ft = FenwickTree([1,2,3,5])
# ft.update(0, 2)
# ft.update(1, 2)
# ft.update(1,3)
#sum for [1,2] low boundary is i - 1.
print(ft.sum(2) - ft.sum(0))




