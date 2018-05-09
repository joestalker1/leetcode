class Solution(object):
    def findRadius(self, houses, heaters):
        heaters = sorted(heaters) + [float('inf')]
        i = r = 0
        for x in sorted(houses):
            while x >= sum(heaters[i:i + 2]) / 2.:
                i += 1
            r = max(r, abs(heaters[i] - x))
        return r

sol = Solution()
#print(sol.findRadius([282475249,622650073,984943658,144108930,470211272,101027544,457850878,458777923],[823564440,115438165,784484492,74243042,114807987,137522503,441282327,16531729,823378840,143542612]))
print(sol.findRadius([1,5], [10]))
print(sol.findRadius([1,5], [2]))
print(sol.findRadius([1,2,3,4],[1,4]))
