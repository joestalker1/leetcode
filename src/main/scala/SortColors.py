class Solution:
    def sortColors(self, nums) -> None:
        #three ways partitioning
        lo = 0
        mid = 0 #first pointer
        hi = len(nums) - 1 #second pointer
        while mid <= hi:
            if nums[mid] == 0:#red
                #swap nums[lo] and nums[mid]
                nums[lo],nums[mid] = nums[mid],nums[lo]
                lo += 1
                mid += 1
            elif nums[mid] == 2:#blue
                #swap nums[mid] and nums[hi]
                nums[mid],nums[hi] = nums[hi],nums[mid]
                hi -= 1
            else:
                mid += 1 # white



sol = Solution()
arr = [2,0,2,1,1,0]
sol.sortColors(arr)
print(arr)
