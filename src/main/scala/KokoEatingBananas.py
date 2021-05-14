class Solution:
    def minEatingSpeed(self, piles, h: int) -> int:
        lo = 1
        hi = sum(piles)

        def can_eat(v):
            return sum([(p - 1) // v + 1 for p in piles]) <= h

        while lo < hi:
            m = lo + (hi - lo) // 2
            if can_eat(m):
                hi = m
            else:
                lo = m + 1
        return lo

sol = Solution()
print(sol.minEatingSpeed(piles = [30,11,23,4,20], H = 6))#23
print(sol.minEatingSpeed(piles = [30,11,23,4,20], H = 5))#30
print(sol.minEatingSpeed(piles = [3,6,7,11], H = 8))#4



