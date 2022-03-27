class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        q = []
        if a != 0:
            heapq.heappush(q,(-a, 'a'))
        if b != 0:
            heapq.heappush(q,(-b, 'b'))
        if c != 0:
            heapq.heappush(q,(-c, 'c'))
        happy = []
        while q:
            freq1,ch1 = heapq.heappop(q)
            if len(happy) >= 2 and happy[-1] == happy[-2] == ch1:
                if not q:
                    return ''.join(happy)
                freq2,ch2 = heapq.heappop(q)
                happy.append(ch2)
                freq2 += 1
                if freq2:
                    heapq.heappush(q, (freq2,ch2))
            happy.append(ch1)
            freq1 += 1
            if freq1:
                heapq.heappush(q, (freq1, ch1))
        return ''.join(happy)