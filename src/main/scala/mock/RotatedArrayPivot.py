class Solution:
    def search(self, nums, target):
        if not nums:
            return -1
        i = 0
        j = len(nums) - 1
        while i <= j:
            mid = i + (j - i) //2
            if nums[mid] == target:
                return mid
            if nums[i] <= nums[mid] and (target < nums[i] or target > nums[mid]):
                i = mid + 1
            elif nums[mid] <= nums[j] and (target < nums[mid] or target > nums[j]):
                j = mid - 1
            elif nums[i] <= nums[mid]:
                j = mid - 1
            elif nums[mid] <= nums[j]:
                i = mid + 1
        return -1

sol = Solution()
#print(sol.search( [4,5,6,7,0,1,2], 0))
print(sol.search( [4,5,6,7,0,1,2], 3))
