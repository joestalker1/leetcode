from heapq import heappop, heappush

class Solution:
    def solution(self, A, B, C):
        q = []
        heappush(q, [-A, 'a'])
        heappush(q, [-B, 'b'])
        heappush(q, [-C, 'c'])
        res = []
        while q:
            freq1,ch1 = heappop(q)
            freq1 = -freq1
            res.append(ch1)
            freq1 -=1
            if freq1 >= 1:
                res.append(ch1)
                freq1 -= 1
            if q:
                freq2, ch2 = heappop(q)
                freq2 = -freq2
                j = 0
                while j < freq2 and j < 2:
                    res.append(ch2)
                    j += 1
                freq2 -= j
                if freq2:
                    heappush(q, [-freq2, ch2])
            if freq1:
                heappush(q,[-freq1, ch1])
        return ''.join(res)


sol = Solution()
print(sol.solution(A = 1, B = 2, C = 3))
print(sol.solution(A = 1, B = 1, C = 6))
