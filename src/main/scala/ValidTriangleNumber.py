import bisect

class Solution:
    def triangleNumber(self, nums):
        if not nums:
            return 0
        nums.sort()
        res = 0
        for i in range(len(nums) - 2):
            k = i + 2
            for j in range(i+1, len(nums) - 1):
                p = bisect.bisect_left(nums, nums[i] + nums[j], k, len(nums))
                if p > j:
                    res += p - j - 1
                    k = p
        return res


sol = Solution()
print(sol.triangleNumber([2,2,3,4]))