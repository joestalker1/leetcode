from collections import defaultdict

class Solution:
    def smallestMissingValueSubtree(self, parents, nums):
        if not parents or not nums:
            return []
        ans = [1] * len(parents)
        if 1 not in nums:
            return ans

        adj_list = defaultdict(list)
        for i in range(len(parents)):
            adj_list[parents[i]].append(i)

        n = len(parents)
        used = set()

        def dfs(adj_list, i, used):
            used.add(nums[i])
            for j in adj_list[i]:
                if nums[j] not in used:
                    dfs(adj_list, j, used)

        # consider subtree in node with value being 1,then its ascendents
        cur = 0
        p = nums.index(1)
        while p != -1:
            if nums[p] in used:
                continue
            dfs(adj_list, p, used)
            while cur + 1 <= n and (cur + 1) in used:
                cur += 1
            ans[p] = cur + 1
            p = parents[p]

        return ans