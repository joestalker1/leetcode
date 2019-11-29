from math import sqrt

class Solution(object):
    def bulbSwitch(self, n):
        if n <= 0:
            return 0
        bulb_on = int(sqrt(n))
        return bulb_on


sol = Solution()
print(sol.bulbSwitch(4))