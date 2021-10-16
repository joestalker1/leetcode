class Solution:
    def minSideJumps(self, obstacles):
        jump = 0
        i = 0
        cur = 2
        while i + 1 < len(obstacles):
            if obstacles[i + 1] == cur:
                jump += 1
                obs = []
                while i < len(obstacles):
                    obs.append(obstacles[i])
                    #if we have all 3 lanes, then we will found farest lane.
                    if 1 in obs and 2 in obs and 3 in obs:
                        break
                    i += 1
                #farest lane
                cur = obs[-1]
                i -= 2
            i += 1
        return jump

sol = Solution()
print(sol.minSideJumps([0,1,0,1,3,1,1,1,0,2,0]))#1
print(sol.minSideJumps([0,2,2,1,0,3,0,3,0,1,0]))#2
print(sol.minSideJumps([0,2,1,0,3,0]))#2
print(sol.minSideJumps([0,1,2,3,0]))#2



