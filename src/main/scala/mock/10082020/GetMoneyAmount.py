class Solution:
    def getMoneyAmount(self, n: int) -> int:
        if n <= 2:
            return n-1

        money = 0
        lo = 1
        hi = n
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if mid == hi:
                break
            money += mid
            lo = mid + 1
        t = 0
        for s in range(lo + (hi-lo)//2, n+1):
            t += s
        return t - money


sol = Solution()
print(sol.getMoneyAmount(3))
print(sol.getMoneyAmount(4))


