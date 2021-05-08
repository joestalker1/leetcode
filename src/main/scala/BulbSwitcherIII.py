class Solution:
    def numTimesAllBlue(self, light):
        res = 0
        #put all buls have been switched on
        max_bulb = 0
        for i in range(len(light)):
            max_bulb = max(max_bulb, light[i])
            #if all left bulsb are less  queue top,then there is case to make l bulb blue
            if max_bulb == i + 1:
                res += 1
        return res


sol = Solution()
print(sol.numTimesAllBlue([1,2,3,4,5,6]))#6
print(sol.numTimesAllBlue([3,2,4,1,5]))#2
print(sol.numTimesAllBlue([2,1,3,5,4]))#3
print(sol.numTimesAllBlue([2, 1, 4, 3, 6, 5]))  # 3
print(sol.numTimesAllBlue([4, 1, 2, 3]))  # 1
print(sol.numTimesAllBlue([2, 1, 3, 5, 4]))  # 3

