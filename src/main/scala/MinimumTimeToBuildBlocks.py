from heapq import heappop,heapify,heappush

class Solution:
    def minBuildTime(self, blocks, split):
        heapify(blocks)
        while len(blocks) > 1:
            bl1 = heappop(blocks)
            bl2 = heappop(blocks)
            new_bl = split + bl2
            heappush(blocks, new_bl)
        return blocks[0]

sol = Solution()
print(sol.minBuildTime([1,1,1,1],100))#201
print(sol.minBuildTime(blocks = [1,2], split = 5))
print(sol.minBuildTime(blocks = [1,2,3], split = 1))