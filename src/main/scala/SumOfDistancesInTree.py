from collections import defaultdict

class Solution:
    def sumOfDistancesInTree(self, n: int, edges):
        if n == 0:
            return 0
        adj_list = defaultdict(list)
        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)

        count = [1] * n
        stsum = [0] * n

        # count sum in subtree node and count
        def get_count(adj_list, node, parent, count, stsum):
            for ch in adj_list[node]:
                if ch == parent:
                    continue
                get_count(adj_list, ch, node, count, stsum)
                count[node] += count[ch]
                stsum[node] += stsum[ch] + count[ch]

        get_count(adj_list, 0, -1, count, stsum)

        # count sum in subtree ch as sum[ch] = sum[parent] +n - 2 * count[ch]
        def get_sum(adj_list, node, parent, count, stsum):
            for ch in adj_list[node]:
                if ch == parent:
                    continue
                stsum[ch] = stsum[node] + n - 2 * count[ch]
                get_sum(adj_list, ch, node, count, stsum)

        get_sum(adj_list, 0, -1, count, stsum)
        return stsum