class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z):
        res = []
        for x in range(1, 1001):
            lo = 1
            hi = 1000
            while lo <= hi:
                m = lo + (hi-lo) // 2
                if customfunction.f(x,m) == z:
                    li = m
                    break
                if customfunction.f(x, m) < z:
                    li = m + 1
                else:
                    hi = m - 1
            for y in range(li, hi + 1):
                c = customfunction.f(x,y)
                if z == c:
                    res.append([x, y])
                if c > z:
                    break
        return res


