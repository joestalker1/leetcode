class SegmetTree:
    def __init__(self, n):
        self.tree = [0] * (4 * n)

    def build(self, arr, tree_index, lo, hi):
        if lo == hi:
            self.tree[tree_index] = arr[lo]
        else:
            mid = lo + (hi - lo) // 2
            self.build(arr, 2 * tree_index + 1, lo, mid)
            self.build(arr, 2 * tree_index + 2, mid + 1, hi)
            self.tree[tree_index] = self.tree[2 * tree_index + 1] + self.tree[2 * tree_index + 2]

    def query(self, tree_index, lo, hi, i, j):
        # arr[i..j]
        if i > hi or j < lo:
            return 0
        if i <= lo and hi <= j:
            return self.tree[tree_index]
        mid = lo + (hi - lo) // 2
        if mid < i:  #
            return self.query(2 * tree_index + 2, mid + 1, hi, i, j)
        elif j <= mid:
            return self.query(2 * tree_index + 1, lo, mid, i, j)
        left = self.query(2 * tree_index + 1, lo, mid, i, mid)
        right = self.query(2 * tree_index + 2, mid + 1, hi, mid + 1, j)
        return left + right

    def update(self, tree_index, lo, hi, arr_index, val):
        if lo == hi:
            self.tree[tree_index] = val
        else:
            mid = lo + (hi - lo) // 2
            if mid < arr_index:
                self.update(2 * tree_index + 2, mid + 1, hi, arr_index, val)
            elif arr_index <= mid:
                self.updatre(2 * tree_index + 1, lo, mid, arr_index, val)
            self.tree[tree_index] = self.tree[2 * tree_index + 1] + self.tree[2 * tree_index + 2]


sg = SegmetTree(4)
sg.build([1, 3, 4, 5], 0, 0, 3)
print(sg.query(0, 0, 3, 1, 2))
print(sg.query(0, 0, 3, 2, 3))
