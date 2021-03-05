from collections import defaultdict
import math

class Solution:
    def minMoves(self, nums, limit):
        n = len(nums)
        dt = defaultdict(int) #dT[i] = T[i] - T[i-1]
        for i in range(n//2):
            a = nums[i]
            b = nums[n - i - 1]
            dt[2] += 2
            dt[min(a, b) + 1] -= 1  # from min(a,b) to min(a,b)+1
            dt[a + b] -= 1
            dt[a + b + 1] += 1
            dt[max(a, b) + limit + 1] += 1
        res = math.inf
        cur_moves = 0
        for s in range(2, 2*limit + 1):
            cur_moves += dt[s]
            res = min(res, cur_moves)
        return res




sol = Solution()
print(sol.minMoves([1, 2, 1, 2], 2))  # 0
print(sol.minMoves([1, 2, 4, 3], 4))  # 1
print(sol.minMoves([1, 2, 2, 1], 2))  # 1
print(sol.minMoves([28, 50, 76, 80, 64, 30, 32, 84, 53, 8], 84))  # 4
