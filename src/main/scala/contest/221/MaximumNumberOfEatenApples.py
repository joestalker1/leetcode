from heapq import heappop, heappush, heapify

class Solution:
    def eatenApples(self, apples, days):
        res = 0
        q = []
        i = 0
        n = len(apples)
        #until having not empty days or i < n
        while q or i < n:
            #add to have most rotten apples
            if i < n:
                heappush(q, [i + days[i], i])
            # remove rotten or empty apples
            while q and (apples[q[0][1]] == 0 or q[0][0] <= i):
                heappop(q)
            if q:
                #eat apple
                res += 1
                j = q[0][1]
                apples[j] -= 1
            i += 1
        return res

sol = Solution()
#37
print(sol.eatenApples([1,10,17,10,12,6,20,8,8,22,14,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,3,5,2,1,0,0,0,0,0,0,23],
[19999,11,18,22,5,2,14,5,20,7,17,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,2,1,4,2,7,0,0,0,0,0,0,1]))
print(sol.eatenApples([2,1,10],[2,10,1]))#4
print(sol.eatenApples([3,0,0,0,0,2], [3,0,0,0,0,2]))#5
print(sol.eatenApples([1,2,3,5,2], [3,2,1,4,2]))#7



