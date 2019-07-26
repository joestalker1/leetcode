import sys

class Solution:
    def increasingTriplet(self, nums):
        if not nums or len(nums) < 3:
            return False
        small = sys.maxsize
        large = sys.maxsize

        for i in range(len(nums)):
            if nums[i] <= small:
                small = nums[i]
            elif nums[i] <= large:
                large = nums[i]
            else:
                return True
        return False

sol = Solution()
print(sol.increasingTriplet([5,1,5,5,2,5,4]))
print(sol.increasingTriplet([1,2,-10,-8,-7]))
print(sol.increasingTriplet([2,5,3,4,5]))
print(sol.increasingTriplet([0,0,10,0,0,1000]))
print(sol.increasingTriplet([1,2,1,2]))
#true,false, true
print(sol.increasingTriplet([1,2,3,1,2,1]))
print(sol.increasingTriplet([5,4,3,2,1]))
print(sol.increasingTriplet([1,2,3,4,5]))



