from collections import defaultdict

class Solution:
    def maximalPathQuality(self, values, edges, maxTime: int) -> int:
        adj_list = defaultdict(list)
        for u,v,t in edges:
            adj_list[u].append([v,t])
            adj_list[v].append([u,t])

        def find_max_quality(adj_list,vert,cur_path,cur_quality,cur_time):
            max_quality = 0
            if vert == 0:
                max_quality = cur_quality
            for nei,t in adj_list[vert]:
                if cur_time + t > maxTime:
                    continue
                new_quality = cur_quality
                if cur_path & (1 << nei) == 0:
                    new_quality += values[nei]
                max_quality = max(max_quality, find_max_quality(adj_list,nei,cur_path | (1 << nei),new_quality,cur_time+ t))
            return max_quality

        return find_max_quality(adj_list,0,1 << 0,values[0], 0)