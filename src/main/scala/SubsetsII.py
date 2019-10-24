class Solution:
    def subsetsWithDup(self, nums):
        if not nums:
            return []
        nums.sort()
        res = []
        def subsets(i, cur):
            if i == len(nums):
                res.append(cur)
                return
            subsets(i + 1, cur)
            new_cur = cur[:]
            new_cur.append(nums[i])
            subsets(i + 1, new_cur)
        subsets(0, [])
        res.sort(key=lambda x:[x, len(x)])
        new_res = []
        for a in res:
            if len(new_res) == 0 or new_res[-1] != a:
                new_res.append(a)
        return new_res


sol = Solution()
print(sol.subsetsWithDup([2,1,2,1,3]))
#[[],[1],[1,1],[1,1,2],[1,1,2,2],[1,1,2,2,3],[1,1,2,3],[1,1,3],[1,2],[1,2,2],[1,2,2,3],[1,2,3],[1,3],[2],[2,2],[2,2,3],[2,3],[3]]
print(sol.subsetsWithDup([4,4,4,1,4]))
#[[],[1],[1,4],[1,4,4],[1,4,4,4],[1,4,4,4,4],[4],[4,4],[4,4,4],[4,4,4,4]]
print(sol.subsetsWithDup([1, 2, 2, 2]))
