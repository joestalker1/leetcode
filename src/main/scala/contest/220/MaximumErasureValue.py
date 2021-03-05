from collections import defaultdict


class Solution:
    def maximumUniqueSubarray(self, nums):
        if not nums:
            return 0
        left = 0
        unique = set()
        max_score = 0
        cur_sum = 0
        for right in range(len(nums)):
            while nums[right] in unique:
                cur_sum -= nums[left]
                unique.discard(nums[left])
                left += 1
            cur_sum += nums[right]
            unique.add(nums[right])
            max_score = max(max_score, cur_sum)
        return max_score


sol = Solution()
print(sol.maximumUniqueSubarray(
    [187, 470, 25, 436, 538, 809, 441, 167, 477, 110, 275, 133, 666, 345, 411, 459, 490, 266, 987, 965, 429, 166, 809,
     340, 467, 318, 125, 165, 809, 610, 31, 585, 970, 306, 42, 189, 169, 743, 78, 810, 70, 382, 367, 490, 787, 670, 476,
     278, 775, 673, 299, 19, 893, 817, 971, 458, 409, 886, 434]))
