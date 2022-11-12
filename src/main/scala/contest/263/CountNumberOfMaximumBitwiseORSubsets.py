class Solution:
    def countMaxOrSubsets(self, nums) -> int:
        if not nums:
            return 0
        max_or_val = 0
        for num in nums:
            max_or_val |= num

        subset_cnt = 0

        def dfs(idx, cur_num):
            nonlocal subset_cnt
            if cur_num == max_or_val:
                subset_cnt += 1
            for i in range(idx, len(nums)):
                dfs(i + 1, cur_num | nums[i])

        dfs(0, 0)
        return subset_cnt


sol = Solution()
print(sol.countMaxOrSubsets([2,2]))#3