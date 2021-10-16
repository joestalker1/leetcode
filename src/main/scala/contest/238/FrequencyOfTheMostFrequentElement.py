class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        cur_sum = k
        l = 0
        for i in range(len(nums)):
            cur_sum += nums[i]
            if cur_sum < nums[i]* (i - l + 1):
                cur_sum -= nums[l]
                l += 1
        return i - l + 1


sol = Solution()
print(sol.maxFrequency([1,2,4], 5))#3
print(sol.maxFrequency([1,4,8,13], 5))#2