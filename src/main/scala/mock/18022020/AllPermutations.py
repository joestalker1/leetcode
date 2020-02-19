class Solution:
    def permute(self, nums):
        if not nums:
            return []

        def perm(i, res):
            if i == len(nums):
                res.append(nums[:])
                return
            for j in range(i, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                perm(i + 1, res)
                nums[i], nums[j] = nums[j], nums[i]

        res = []
        perm(0, res)
        return res


sol = Solution()
print(sol.permute([1, 2, 3]))
