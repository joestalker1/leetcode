from heapq import heappush,heappop


class Solution:
    def lastStoneWeight(self, stones):
        if not stones:
            return None
        weight = []
        for stone in stones:
            heappush(weight, -stone)

        while len(weight) > 1:
            x = heappop(weight)
            y = heappop(weight)
            if x == y:
                continue
            heappush(weight, x - y)
        return -weight[0]


sol = Solution()
print(sol.lastStoneWeight([2,7,4,1,8,1]))






