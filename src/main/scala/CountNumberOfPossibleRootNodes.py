from collections import defaultdict

class Solution:
    def rootCount(self, edges, guesses, k: int) -> int:
        # assert self._rootCount(edges = [[0,1],[1,2],[1,3],[4,2]], guesses = [[1,3],[0,1],[1,0],[2,4]], k = 3) == 3, 'test1'
        # assert self._rootCount(edges = [[0,1],[1,2],[2,3],[3,4]], guesses = [[1,0],[3,4],[2,1],[3,2]], k = 1) == 5, 'test2'
        # assert self._rootCount(edges = [[0,1]], guesses = [[1,0],[0,1]], k = 1) == 2, 'test3'
        return self._rootCount(edges, guesses, k)

    def _rootCount(self, edges, guesses, k: int) -> int:
        adj_lst = defaultdict(list)
        for a, b in edges:
            adj_lst[a].append(b)
            adj_lst[b].append(a)
        par_node = defaultdict(set)
        for a, b in guesses:
            par_node[a].add(b)
        n = len(edges) + 1
        parents = [0] * n
        guesess_cnt = 0
        ans = 0

        def fill_parent(adj_lst, parents, node, parent):
            parents[node] = parent
            for child in adj_lst[node]:
                if child == parent:
                    continue
                fill_parent(adj_lst, parents, child, node)

        def dfs(adj_lst, par_node, node, parent, guesess_cnt):
            nonlocal ans
            cnt = guesess_cnt
            if node in par_node[parent]:
                cnt -= 1
            if parent in par_node[node]:
                cnt += 1
            if cnt >= k:
                ans += 1
            for child in adj_lst[node]:
                if child == parent:
                    continue
                dfs(adj_lst, par_node, child, node, cnt)

        fill_parent(adj_lst, parents, 0, -1)
        # count guessed edges for root 0
        for v in range(1, n):
            p = parents[v]
            if v in par_node[p]:
                guesess_cnt += 1

        if guesess_cnt >= k:
            ans += 1
        # count the guessed edges for subtrees of 0
        for child in adj_lst[0]:
            dfs(adj_lst, par_node, child, 0, guesess_cnt)
        return ans




