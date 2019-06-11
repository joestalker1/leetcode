class Solution:
    def swap(self, nums, i1, i2):
        t = nums[i1]
        nums[i1] = nums[i2]
        nums[i2] = t

    def swap_pairs(self, nums, i1, i2):
        self.swap(nums, i1, i2)
        if i1+1 < len(nums) and (i2+1) < len(nums):
            self.swap(nums, i1 + 1, i2 + 1)


    def find_greater(self, nums, a, i):
        while i < len(nums) and nums[i] <= a:
            i += 1
        return i if i < len(nums) else -1

    def wiggleSort(self, nums):
        if not nums:
            return
        mean = sum(nums)
        mean = mean / len(nums)
        i = 0
        j = 0
        while i < len(nums) - 1:
            if nums[i] <= mean and j < len(nums):
                self.swap(nums, i, j)
                j += 1
            i += 1

        for i in range(len(nums)):
            if i % 2 == 1 and j < len(nums):
                self.swap(nums, i, j)
                j += 1



sol = Solution()
arr = [4,5,5,5,5,6,6,6]
sol.wiggleSort(arr)
# print(arr)
# arr = [1,1,2,1,2,2,1]
# sol.wiggleSort(arr)
# print(arr)
# arr = [4,5,5,6]
# sol.wiggleSort(arr)
# print(arr)
# arr = [1,1,1,2,2,2]
# sol.wiggleSort(arr)
# print(arr)
# arr = [1, 5, 1, 1, 6, 4]
# sol.wiggleSort(arr)
# print(arr)
