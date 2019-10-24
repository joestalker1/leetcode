class Solution:
    def minEatingSpeed(self, piles, H):
        if not piles or H == 0:
            return 0
        k = max(piles)
        lo = 1
        hi = sum(piles)
        while lo <= hi:
            speed = lo + (hi - lo) // 2
            hours = 0
            for i in range(len(piles)):
                if piles[i] <= speed:
                    hours += 1
                else:
                    #eating piles
                    hours += (piles[i] // speed)
                    if piles[i] % speed != 0:
                        hours += 1
            if hours <= H:
                k = min(speed, k)
                hi = speed - 1
            else:
                lo = speed + 1
        return k

sol = Solution()
print(sol.minEatingSpeed(piles = [30,11,23,4,20], H = 6))#23
print(sol.minEatingSpeed(piles = [30,11,23,4,20], H = 5))#30
print(sol.minEatingSpeed(piles = [3,6,7,11], H = 8))#4



