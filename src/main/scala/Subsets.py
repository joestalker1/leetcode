class Solution:
    def subsets(self, nums: 'List[int]') -> 'List[List[int]]':
        if not nums:
            return []
        n = 2 ** len(nums)
        res = [[]]
        for x in range(1, n):
            a = x
            pos = len(nums) - 1
            subset = []
            while a > 0:
                if a & 1:
                    subset.insert(0, nums[pos])
                a = a >> 1
                pos -= 1
            res.append(subset)
        return res


sol = Solution()
print(sol.subsets([1, 2, 3]))
