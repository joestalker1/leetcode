from heapq import heappop,heappush

class Solution:
    def maxEvents(self, events):
        #shorter events come first
        sorted_by_start = sorted(events,key=lambda x:x[0])
        cnt = 0
        pq = []
        j = 0
        for d in range(1, 10**5+1):
            #remove the events that have been finished
            while pq and pq[0] < d:
                heappop(pq)
            #add the events that started this day
            while j < len(sorted_by_start) and sorted_by_start[j][0] == d:
                heappush(pq, sorted_by_start[j][1])
                j += 1
            if pq:
                heappop(pq)
                cnt += 1
        return cnt


sol = Solution()
print(sol.maxEvents([[52,79],[7,34]]))#2
print(sol.maxEvents([[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7]]))#7
print(sol.maxEvents([[1,4],[4,4],[2,2],[3,4],[1,1]]))#4
print(sol.maxEvents([[1,2],[2,3],[3,4]]))#3


