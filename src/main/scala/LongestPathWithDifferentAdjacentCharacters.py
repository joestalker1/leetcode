from collections import defaultdict

class Solution:
    def longestPath(self, parent, s: str) -> int:
        adj_list = defaultdict(list)
        for i, p in enumerate(parent):
            if p == -1:
                continue
            adj_list[p].append(i)

        max_path = 1

        def dfs(adj_list, v):
            nonlocal max_path
            first_len = 0
            second_len = 0
            for child in adj_list[v]:
                # call if some decendants form max_path
                cur_len = dfs(adj_list, child)
                if s[v] == s[child]:
                    continue
                if first_len < cur_len:
                    second_len = first_len
                    first_len = cur_len
                elif second_len < cur_len:
                    second_len = cur_len
            max_path = max(max_path, 1 + first_len + second_len)
            return 1 + first_len

        dfs(adj_list, 0)
        return max_path