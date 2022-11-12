import heapq

class Solution:
    def getSkyline(self, buildings):
        if not buildings:
            return []
        events = []
        for x1,x2,height in buildings:
            events.append([x1,height])
            events.append([x2, -height])
        events.sort()
        skyline = []
        #past is when house is gone
        live,past = [],[]
        i = 0
        while i < len(events):
            cur_x = events[i][0]
            while i < len(events) and events[i][0] == cur_x:
                height = events[i][1]
                if height > 0:
                    heapq.heappush(live, -height)
                else:
                    heapq.heappush(past, height)
                i += 1
            while past and live and past[0] == live[0]:
                heapq.heappop(live)
                heapq.heappop(past)
            max_height = -live[0] if live else 0
            if not skyline or skyline[-1][1] != max_height:
                skyline.append([cur_x, max_height])
        return skyline