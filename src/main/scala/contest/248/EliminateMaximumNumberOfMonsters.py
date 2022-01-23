import heapq

class Solution:
    def eliminateMaximum(self, dist, speed) -> int:
        attack = []
        for i in range(len(dist)):
            heapq.heappush(attack, dist[i]/speed[i])
        t = 1
        killed = 0
        while attack:
            #can kill on monster
            killed += 1
            heapq.heappop(attack)
            if attack and attack[0] <= t:
                return killed
            #charge weapon
            t += 1
        return killed

sol = Solution()
print(sol.eliminateMaximum([1,1,2,3], [1,1,1,1]))#1

