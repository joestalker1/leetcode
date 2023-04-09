from collections import defaultdict

class Solution:
    def maxOutput(self, n: int, edges, price) -> int:
        # if n == 1:
        #     return price[0]
        adj_list = defaultdict(list)
        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)
        subtree_sum = [0] * n

        def fill_sum(adj_list, node, par, subtree_sum):
            max_sum = 0
            for child in adj_list[node]:
                if child == par:
                    continue
                max_sum = max(max_sum, fill_sum(adj_list, child, node, subtree_sum))
            subtree_sum[node] = max_sum + price[node]
            return subtree_sum[node]

        fill_sum(adj_list, 0, -1, subtree_sum)

        def find_max(adj_list, node, par, par_distrib, subtree_sum):
            best_child = -1
            max_path1 = 0
            max_path2 = 0
            for v in adj_list[node]:
                if v == par:
                    continue
                if subtree_sum[v] > max_path1:
                    max_path2 = max_path1
                    best_child = v
                    max_path1 = subtree_sum[v]
                elif subtree_sum[v] > max_path2:
                    max_path2 = subtree_sum[v]
            path1 = max_path1
            path2 = par_distrib
            max_cost = max(path1, path2)
            for v in adj_list[node]:
                if v == par:
                    continue
                # take new par_distrib as price[node] + (max_sum of subtree or previous par_distrib)
                # if child is best_child, we take the second max path.
                if v == best_child:
                    max_cost = max(max_cost,
                                   find_max(adj_list, v, node, price[node] + max(max_path2, par_distrib), subtree_sum))
                else:
                    max_cost = max(max_cost,
                                   find_max(adj_list, v, node, price[node] + max(max_path1, par_distrib), subtree_sum))
            return max_cost

        return find_max(adj_list, 0, -1, 0, subtree_sum)