from heapq import heappush,heappop

class Solution:
    def topKFrequent(self, nums, k):
        if not nums or k > len(nums):
            return []
        if k == len(nums):
            return nums
        m = {}
        for i in range(len(nums)):
            if nums[i] not in m:
                m[nums[i]] = 0
            m[nums[i]] += 1
        h = []
        for a,b in m.items():
            if len(h) == k:
                if h[0][0] < b:
                    heappop(h)
                    heappush(h, (b, a))
            else:
                heappush(h, (b, a))
        return [h[i][1] for i in range(len(h))]

sol = Solution()
print(sol.topKFrequent([1,1,1,2,2,3], 2))