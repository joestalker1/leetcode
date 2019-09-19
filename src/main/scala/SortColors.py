class Solution:
    def sortColors(self, nums):
        if not nums:
            return nums
        p0 = 0
        p2 = len(nums) - 1
        cur = 0
        while cur <= p2:
            if nums[cur] == 0:
                nums[p0], nums[cur] = nums[cur], nums[p0]
                cur += 1
                p0 += 1
            elif nums[cur] == 2:
                nums[p2], nums[cur] = nums[cur], nums[p2]
                p2 -= 1
            else:
                cur += 1


sol = Solution()
arr = [2,0,2,1,1,0]
sol.sortColors(arr)
print(arr)
