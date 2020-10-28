from collections import defaultdict
import bisect

class Solution:
    def shortestDistanceColor(self, colors, queries):
        clr_to_pos = defaultdict(list)
        for i,clr in enumerate(colors):
            clr_to_pos[clr].append(i)
        res = []
        for qr in queries:
            i,clr = qr
            if clr not in clr_to_pos:
                res.append(-1)
                continue
            cand = clr_to_pos[clr]
            j = bisect.bisect_left(cand, i)
            d1 = abs(i - cand[j])
            d2 = abs(i - cand[j-1]) if j - 1 >= 0 else float('inf')
            if d1 <= d2:
                res.append(cand[j])
            else:
                res.append(cand[j-1])
        return res


