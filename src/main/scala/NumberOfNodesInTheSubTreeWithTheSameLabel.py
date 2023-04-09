from collections import defaultdict

class Solution:
    def countSubTrees(self, n: int, edges, labels: str):
        n = len(labels)
        adj_lst = defaultdict(list)
        for a,b in edges:
            adj_lst[a].append(b)
            adj_lst[b].append(a)

        def dfs(adj_lst, par, v, node_to_cnt):
            node_to_cnt[v] = 1
            node_labels = {labels[v]:1}
            for nei in adj_lst[v]:
                if nei == par:
                    continue
                nei_labels = dfs(adj_lst, v,nei, node_to_cnt)
                for k in nei_labels:
                    if k not in node_labels:
                        node_labels[k] = 0
                    node_labels[k] += nei_labels[k]
            node_to_cnt[v] = node_labels[labels[v]]
            return node_labels

        node_to_cnt = [0] * n
        dfs(adj_lst,0, 0, node_to_cnt)
        return node_to_cnt