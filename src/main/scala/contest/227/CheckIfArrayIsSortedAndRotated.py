class Solution:
    def check(self, nums):
        if not nums or len(nums) == 1:
            return True
        c = 0
        # only first and last items can be in decreasing order
        for i in range(len(nums)):
            if nums[i] > nums[(i + 1) % len(nums)]:
                c += 1
            if c > 1:
                return False
        return True


sol = Solution()
print(sol.check([2,1,3,4]))#false
print(sol.check([3,4,5,1,2]))#true
print(sol.check([6,10,6]))#true
