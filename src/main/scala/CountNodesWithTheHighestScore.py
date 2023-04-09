from collections import defaultdict

class Solution:
    def countHighestScoreNodes(self, parents) -> int:
        if not parents:
            return 0
        score = [0] * len(parents)
        adj_list = defaultdict(list)
        for i in range(len(parents)):
            adj_list[parents[i]].append(i)

        def dfs(adj_list, score, v):
            prod = 1
            node_cnt = 1
            for u in adj_list[v]:
                # count product for child substree
                cur_cnt = dfs(adj_list, score, u)
                prod *= cur_cnt
                node_cnt += cur_cnt
                # len(parents) - node_cnt is number of nodes in parent's subtree
            score[v] = prod * max(1, len(parents) - node_cnt)
            return node_cnt

        dfs(adj_list, score, 0)
        max_score = max(score)
        return len([sc for sc in score if sc == max_score])