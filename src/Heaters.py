import bisect
import sys


class Solution(object):
    def findRadius(self, houses, heaters):
        heaters = sorted(heaters)
        result = 0
        for house in houses:
            index = bisect.bisect_left(heaters, house)
            if index < 0:
                index = -(index + 1)
            dist1 = sys.maxsize
            if 0 <= index - 1 < len(houses) :
                dist1 = houses[index - 1]
            dist2 = sys.maxsize
            if index < len(heaters):
                dist2 = heaters[index] - house
            result = max(result,min(dist1, dist2))
        return result


sol = Solution()
print(sol.findRadius([282475249,622650073,984943658,144108930,470211272,101027544,457850878,458777923],[823564440,115438165,784484492,74243042,114807987,137522503,441282327,16531729,823378840,143542612]))
print(sol.findRadius([1,2,3,4], [1, 4]))
print(sol.findRadius([1],[1,2,3,4]))
print(sol.findRadius([1,5], [10]))