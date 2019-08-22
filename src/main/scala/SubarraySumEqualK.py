from collections import defaultdict

class Solution:
    def subarraySum(self, nums, k):
        sums = defaultdict(lambda: 0)
        sums[0] = 1
        cur_sum = 0
        total = 0

        for i in range(len(nums)):
            cur_sum += nums[i]
            if (cur_sum - k) in sums.keys():
                total += sums[cur_sum - k]
            sums[cur_sum] += 1
        return total

    
sol = Solution()

print(sol.subarraySum([1, 2, 3], 3))
print(sol.subarraySum([0, 0, 0], 0))
