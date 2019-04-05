class Solution:
    def twoSum(self, nums, target):
        if not nums:
            return []
        m = {}
        for i in range(len(nums)):
            a = target - nums[i]
            if a in m:
                return [m[a], i]
            m[nums[i]] = i
        return None


sol = Solution()
print(sol.twoSum([2, 7, 11, 15], 9))
