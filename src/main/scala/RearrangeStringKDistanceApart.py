from collections import Counter
from heapq import heappop,heappush,heapify


class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k == 0:
            return s
        freq = Counter(s)
        q = [(-cnt, ch) for ch,cnt in freq.items()]
        st = []
        heapify(q)
        res = []
        while q:
            for _ in range(k):
                if not q and st:
                    return ''
                if q:
                    cnt,ch = heappop(q)
                    res.append(ch)
                    if cnt < -1:
                        st.append((cnt+1,ch))
            while st:
                heappush(q, st.pop())
        return ''.join(res)