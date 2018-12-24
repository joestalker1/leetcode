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
arr4 = [4,5,6,7,8,1,2,3]
print(sol.search(arr4, 8))

arr3 = [5,1,3]
print(sol.search(arr3, 5))
print(sol.search(arr3, 3))

arr1 = [4,5,6,7,0,1,2]

print(sol.search(arr1, 0))

arr2 = [4,5,6,7,0,1,2]
print(sol.search(arr2, 3))