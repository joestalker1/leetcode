from collections import defaultdict

class Solution:
    def minTime(self, n: int, edges, hasApple) -> int:
        if not edges:
            return 0
        adj_list = defaultdict(list)
        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)

        def count_time(adj_list, parent, v):
            total_time = 0
            for child in adj_list[v]:
                if child == parent:
                    continue
                child_time = count_time(adj_list, v, child)
                if child_time or hasApple[child]:
                    total_time += child_time + 2
            return total_time

        return count_time(adj_list, -1, 0)