class Solution:
    def findMin(self, nums):
        if not nums:
            return

        if len(nums) == 1:
            return nums[0]

        if nums[0] < nums[len(nums) - 1]:
            return nums[0]

        def find_inflection_index(s, e):
            if s > e:
                return s
            mid = s + (e - s) // 2

            if mid + 1 < len(nums) and nums[mid + 1] < nums[mid]:
                return mid + 1

            if nums[mid - 1] > nums[mid]:
                return mid

            if nums[0] < nums[mid]:
                s = mid + 1
            else:
                e = mid - 1
            return find_inflection_index(s, e)

        ind = find_inflection_index(0, len(nums) - 1)
        return nums[ind]


sol = Solution()
print(sol.findMin([3,1,2]))
print(sol.findMin([3,4,5,1,2]))
print(sol.findMin([4,5,6,7,0,1,2]))
