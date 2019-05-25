class Solution:
    def find_least(self, nums, target):
        s = 0
        e = len(nums) - 1
        res = -1
        while s <= e:
            mid = s + (e - s) // 2
            if nums[mid] < target:
                s = mid + 1
            else:
                if nums[mid] == target:
                    res = mid
                e = mid - 1
        return res

    def find_greatest(self, nums, target):
        s = 0
        e = len(nums) - 1
        res = -1
        while s <= e:
            mid = s + (e - s) // 2
            if nums[mid] > target:
                e = mid - 1
            else:
                if nums[mid] == target:
                    res = mid
                s = mid + 1
        return res

    def searchRange(self, nums, target):
        if not nums:
            return [-1, -1]
        return [self.find_least(nums, target), self.find_greatest(nums, target)]

sol = Solution()
print(sol.searchRange([5,7,7,8,8,10], 8))
print(sol.searchRange([1], 1))
print(sol.searchRange([5,5], 5))
print(sol.searchRange([5,7,7,8,8,10], 6))