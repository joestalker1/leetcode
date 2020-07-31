from heapq import heappush, heappop

class Solution:
    def longestSubarray(self, nums, limit):
        if not nums:
            return 0
        min_num = []
        max_num = []
        max_len = 0
        left = 0

        for right in range(len(nums)):
            heappush(min_num, (nums[right], right))
            heappush(max_num,  (-nums[right], right))
            while abs(max_num[0][0] + min_num[0][0]) > limit and left < right:
                left += 1
                while min_num[0][1] < left:
                    heappop(min_num)
                while max_num[0][1] < left:
                    heappop(max_num)
            max_len = max(max_len, right - left + 1)
        return max_len


sol = Solution()
print(sol.longestSubarray([4, 2, 2, 2, 4, 4, 2, 2], 0))
print(sol.longestSubarray([10, 1, 2, 4, 7, 2], 5))
