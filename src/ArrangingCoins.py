import math

class Solution:
    def arrangeCoins(self, n):
        return int((-1 + math.sqrt(1 + 8 * n)) / 2)



sol = Solution()
print(sol.arrangeCoins(6))
#print(sol.arrangeCoins(1))
#print(sol.arrangeCoins(2))
print(sol.arrangeCoins(8))
print(sol.arrangeCoins(5))
