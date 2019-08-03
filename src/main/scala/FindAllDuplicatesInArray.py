class Solution:
    def findDuplicates(self, nums):
        if not nums:
            return []
        res = []
        for z in nums:
            i = abs(z) - 1
            if nums[i] < 0:
                res.append(i + 1)
            else:
                nums[i] = -nums[i]
        return res


sol = Solution()
print(sol.findDuplicates([10,2,5,10,9,1,1,4,3,7]))
print(sol.findDuplicates([1]))
print(sol.findDuplicates([4,3,2,7,8,2,3,1]))

        
