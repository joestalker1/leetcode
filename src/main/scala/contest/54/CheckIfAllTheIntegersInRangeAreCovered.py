class Solution:
    def isCovered(self, ranges, left: int, right: int):
        if not ranges:
            return False
        ranges.sort(key=lambda x: x[0])
        res = []
        for s,e in ranges:
            if not res or res[-1][1] < s:
                res.append([s,e])
            else:
                res[-1] = [res[-1][0],max(res[-1][1], e)]
        for x in range(left, right + 1):
            s = 0
            e = len(res) - 1
            f = False
            while s <= e:
                m = s + (e - s) // 2
                if res[m][0] <= x and x <= res[m][1]:
                    f = True
                    break
                elif x > res[m][0]:
                    s = m + 1
                else:
                    e = m - 1

            if not f:
                return False
        return True

sol = Solution()
print(sol.isCovered([[16,18],[8,40],[12,23],[5,19],[11,11]],17,34))#true
print(sol.isCovered([[1,50]],1,50))#true
