class Solution:
    def findErrorNums(self, nums):
        arr = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            a = nums[i]
            arr[a] += 1
        res = []
        for i in range(1, len(arr)):
            if arr[i] == 0 or arr[i] == 2:
                res.append(i)
        return res.sort()



