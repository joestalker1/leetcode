class Solution:
    def wiggleSort(self, nums):
        if not nums:
            return nums
        # it should have even length
        nums.sort()
        i = 0
        j = len(nums) // 2
        while j < len(nums):
            if i > 0:
                nums[i],nums[j] = nums[j],nums[i]
                nums[i],nums[i+1] = nums[i+1],nums[i]
            else:
                nums[i+1],nums[j] = nums[j],nums[i+1]
            i += 2
            j += 1


sol = Solution()
print(sol.wiggleSort([3,5,2,1,6,4]))




