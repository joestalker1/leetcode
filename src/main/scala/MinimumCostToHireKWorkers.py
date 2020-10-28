from heapq import heappop, heappush

class Solution:
    def mincostToHireWorkers(self, quality, wage, K: int) -> float:
        # consider with min coefficient
        workers = sorted([[w/q,q,w] for q,w in zip(quality, wage)])
        res = float('inf')
        pool = []
        sumq = 0
        for r, q, w in workers:
            # candidates with maximal quality first
            heappush(pool, -q)
            sumq += q
            if len(pool) > K:
                # remove redundant
                a = heappop(pool)
                sumq += a # subtract a from sum
            if len(pool) == K:
                res = min(res, r * sumq)
        return res


sol = Solution()
print(sol.mincostToHireWorkers([32,43,66,9,94,57,25,44,99,19], [187,366,117,363,121,494,348,382,385,262], 4)) #1528.00000
