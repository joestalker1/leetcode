class Solution:
    def largestDivisibleSubset(self, nums):
        if not nums:
            return []
        nums.sort()
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[i] % nums[j] == 0:
                    dp[i] += 1
        max_index = -1
        max_len = max(dp)
        for i in range(len(dp)):
            if dp[i] == max_len:
                max_index = i
                break
        return list(filter(lambda x: nums[max_index] % x == 0, nums[0:max_index + 1]))



sol = Solution()
#print(sol.largestDivisibleSubset([1]))
print(sol.largestDivisibleSubset([1,2,4,8]))