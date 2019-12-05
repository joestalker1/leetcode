class Solution(object):
    def dailyTemperatures(self, t):
        if not t:
            return []
        res = [0] * len(t)
        wait = []
        for i in range(len(t)):
            while wait and t[wait[-1]] < t[i]:
                res[wait[-1]] = i - wait[-1]
                wait.pop()
            wait.append(i)
        return res

sol = Solution()
print(sol.dailyTemperatures([89,62,70,58,47,47,46,76,100,70]))#[8,1,5,4,3,2,1,1,0,0]


