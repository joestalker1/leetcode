class Solution:
    def countSubarrays(self, nums, k: int) -> int:
        cnt = 0
        pr_sum = 0
        l = 0
        for i in range(len(nums)):
            pr_sum += nums[i]
            while pr_sum * (i - l + 1) >= k:
                pr_sum -= nums[l]
                l += 1
            cnt += (i - l + 1)
        return cnt

sol = Solution()
#print(sol.countSubarrays([2,1,4,3,5],10))#6
print(sol.countSubarrays([1,1,1],5))