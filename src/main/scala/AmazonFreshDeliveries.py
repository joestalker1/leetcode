from heapq import heappop, heappush


class Solution:
    def kclosest(self, xy, k):
        q = []
        for x, y in xy:
            if len(q) < k:
                heappush(q, [-(x * x + y * y), [x, y]])
            else:
                max_r = -q[0][0]
                r = x * x + y * y
                if r < max_r:
                    heappop(q)
                    heappush(q, -r)
        return [coord for r,coord in q]


sol = Solution()
print(sol.kclosest([ [1, 2] , [1, -1], [3, 4] ], 2))
