class Solution:
    def uniquePairs(self, nums, target):
        if not nums:
            return 0
        left = 0
        right = len(nums) - 1
        pairs = 0
        while left < right:
            sums = nums[left] + nums[right]
            if sums == target:
                pairs+=1
                a = nums[left]
                b = nums[right]
                while left < right and a == nums[left] and b == nums[right]:
                    left += 1
                    right -= 1
            elif sums > target:
                right -= 1
            else:
                left += 1
        return pairs


sol = Solution()
print(sol.uniquePairs(nums = [1, 1], target = 2))
print(sol.uniquePairs(nums = [1, 1, 2, 45, 46, 46], target = 47))
