from collections import defaultdict
from heapq import heappush, heappop

class Solution:
    def reorganizeString(self, S):
        if not S:
            return ''
        freq = defaultdict(int)
        for ch in S:
            freq[ch] += 1
        q = []
        for ch,fr in freq.items():
            heappush(q, [-fr, ch])
        res = []
        while q:
            f1,ch1 = heappop(q)
            if res and res[-1] == ch1:
                return ''
            res.append(ch1)
            f1 += 1
            if q:
                f2,ch2 = heappop(q)
                res.append(ch2)
                f2 += 1
                if f2:
                    heappush(q, [f2, ch2])
            if f1:
                heappush(q, [f1,ch1])
        return ''.join(res)


sol = Solution()
print(sol.reorganizeString(S = "aaab"))
print(sol.reorganizeString(S = "aab"))





