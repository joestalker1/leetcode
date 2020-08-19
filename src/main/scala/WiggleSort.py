class Solution:
    def wiggleSort(self, nums):
        if not nums:
            return nums
        # it should have even lengt
        nums.sort()
        for i in range(1, len(nums)-1, 2):
            #exchange neigbour with step 2
            nums[i],nums[i+1] = nums[i+1],nums[i]
        return nums
