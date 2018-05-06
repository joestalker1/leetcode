import sys
class Solution:
    def maxCount(self, m, n, ops):
        if not ops:
            return m * n
        min_i = sys.maxsize
        min_j = sys.maxsize
        for op in ops:
            i1 = op[0]
            j1 = op[1]
            if min_i > i1:
                min_i = i1
            if min_j > j1:
                min_j = j1
        return min_i * min_j

sol = Solution()
print(sol.maxCount(3,3, [[2,2],[3,3]]))