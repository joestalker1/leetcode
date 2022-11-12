class Solution(object):
    def nextPermutation(self, nums):
        if not nums:
            return
        i = len(nums) - 2
        # find first increasing order item nums[i] < nums[i+1]
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        if i >= 0:
            # find the least bigger item
            j = len(nums) - 1
            #find leftmost nums[j] > nums[i]
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1
            nums[i],nums[j] = nums[j], nums[i]
        # reverse
        i += 1
        j = len(nums) - 1
        while i < j:
            nums[i],nums[j] = nums[j],nums[i]
            i += 1
            j -= 1


sol = Solution()
arr = [1,2,3]
sol.nextPermutation(arr)
print(arr)