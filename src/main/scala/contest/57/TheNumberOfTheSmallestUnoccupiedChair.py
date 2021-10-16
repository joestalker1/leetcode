from heapq import heappop,heappush

class Solution:
    def smallestChair(self, times, targetFriend: int) -> int:
        n = len(times)
        chairs = [i for i in range(n)]
        wait = []
        arr = [[times[i][0],times[i][1],i] for i in range(n)]
        arr.sort(key=lambda x:x[0])
        for s,e,i in arr:
            while wait and wait[0][0] <= s:
                t,j,c = heappop(wait)
                heappush(chairs, c)
            c = heappop(chairs)
            if i == targetFriend:
                return c
            heappush(wait,[e,i,c])

sol = Solution()
print(sol.smallestChair([[3,10],[1,5],[2,6]], 0))#2
