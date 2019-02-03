from collections import defaultdict

class Solution:
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums or len(nums) == 0:
            return 0
        sums = [0] * (len(nums) + 1)
        sums[0] = nums[0]
        for j in range(1, len(sums)):
            sums[j] = sums[j - 1] + nums[j - 1]
        total = 0
        for s in range(len(nums)):
            for e in range(s + 1, len(sums)):
                if sums[e] - sums[s] == k:
                    total += 1
        return total
        #
        # sums = defaultdict(lambda: 0)
        # sums[0] = 1
        # cur_sum = 0
        # total = 0
        #
        # for i in range(len(nums)):
        #     cur_sum += nums[i]
        #     if (cur_sum - k) in sums.keys():
        #         total += sums[cur_sum - k]
        #     sums[cur_sum] += 1
        # return total

    
sol = Solution()

print(sol.subarraySum([1, 2, 3], 3))
print(sol.subarraySum([0, 0, 0], 0))
