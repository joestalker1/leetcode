from heapq import heappush,heappop

class Solution:
    def minMeetingRooms(self, intervals):
        if not intervals:
            return 0
        q = []
        intervals.sort(lambda x:x[0])
        for s,e in intervals:
            heappush(q,e)
        for i in range(1, len(intervals)):
            if i[1] >= q[0]:
                heappop(q)
            else:
                heappush(q, i[1])
        return len(q)
