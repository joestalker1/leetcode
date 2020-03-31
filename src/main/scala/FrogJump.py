class SparseArray:
    def __init__(self, cols):
        self.rows = dict()
        self.cols = cols

    def row(self, i):
        if i in self.rows:
            return self.rows[i]
        self.rows[i] = [False] * self.cols
        return self.rows[i]

    def len(self):
        return len(self.rows.keys())


class Solution:
    def canCross(self, stones):
        if not stones:
            return False
        stone_to_pos = {stones[i]: i for i in range(len(stones))}
        dp = SparseArray(len(stones))  # sparse array
        dp.row(0)[0] = True
        dp.row(stones[1])[1] = True
        max_row = 2
        for i, stone in enumerate(stones):
            for t in range(1, max_row + 1):
                prev = stone - t
                if prev <= 0:
                    break
                if prev not in stone_to_pos:
                    continue
                j = stone_to_pos[prev]
                k1 = t + 1
                k2 = t
                k3 = t - 1
                if dp.row(k1)[j] or dp.row(k2)[j] or k3 > 0 and dp.row(k3)[j]:
                    max_row = max(max_row, k1)
                    dp.row(t)[i] = True
        return any([dp.row(i)[-1] for i in range(dp.len())])


sol = Solution()
print(sol.canCross([0, 1, 3, 6, 10, 15, 19, 21, 24, 26, 30, 33]))  # true
print(sol.canCross([0, 1, 2147483647]))  # false
print(sol.canCross([0,2]))#false
print(sol.canCross([0, 1, 3, 5, 6, 8, 12, 17]))  # True
print(sol.canCross([0, 1, 2, 3, 4, 8, 9, 11]))  # false
