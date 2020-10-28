from collections import defaultdict


class Solution:
    def numberOfPatterns(self, m, n):
        patterns = 0
        adj_list = defaultdict(list)
        adj_list[1] = [2,4,5]
        adj_list[2] = [1,3,5,4,6]
        adj_list[3] = [2,6,5]
        adj_list[4] = [1,5,2,8,7]
        adj_list[5] = [1,2,3,4,6,7,8,9]
        adj_list[6] = [3,2,5,8,9]
        adj_list[7] = [4,5,8]
        adj_list[8] = [7,4,5,6,9]
        adj_list[9] = [5,6,8]

        def dfs(adj_list, src, target, moved, seen):
            if src == target:
                return True
            for nei in adj_list[src]:
                if nei == target:
                    return True
                if nei in seen:
                    continue
                seen.add(nei)
                if nei in moved and dfs(adj_list, nei, target, moved, seen):
                    return True
            return False


        def backtrack(adj_list, f, moved, uniq, res):
            nonlocal patterns
            if m <= len(moved) <= n:
                print(moved)
                res.append(res[::])
                s = ''.join([str(a) for a in moved])
                if s not in uniq:
                    uniq.add(s)
                    patterns += 1
                if len(moved) == n:
                    return
            for i in range(1, 10):
                if i == f:
                    continue
                if dfs(adj_list, f, i,moved, set()):
                    moved.append(i)
                    backtrack(adj_list, i, moved,uniq, res)
                    moved.pop(-1)
        uniq = set()
        res = []
        for i in range(1, 10):
            backtrack(adj_list, i, [i], uniq, res)
        return len(res)

sol = Solution()
print(sol.numberOfPatterns(1,2))







