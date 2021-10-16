from collections import defaultdict,Counter

class Solution:
    def largestPathValue(self, colors: str, edges) -> int:
        if not colors or not edges:
            return -1
        adj_lst = defaultdict(list)
        num_vert = len(colors)
        in_degree = [0] * num_vert
        for v, u in edges:
            adj_lst[v].append(u)
            in_degree[u] += 1

        seen = [0] * num_vert

        def is_cycle(adj_lst, u, seen):
            seen[u] = 1
            for v in adj_lst[u]:
                if seen[v] == 1:
                    return True
                if seen[v] == 0 and is_cycle(adj_lst, v, seen):
                    return True
            return False

        for v in range(num_vert):
            if seen[v] == 0 and is_cycle(adj_lst, v, seen):
                return -1
        top_sort_queue = []
        for v in range(num_vert):
            if in_degree[v] == 0:
                top_sort_queue.append(v)
                break
        top_sorted_vert = []
        while top_sort_queue:
            v = top_sort_queue.pop(0)
            top_sorted_vert.append(v)
            for u in adj_lst[v]:
                in_degree[u] -= 1
                if in_degree[u] == 0:
                    top_sort_queue.append(u)
        top_sorted_vert.reverse()
        l = 0
        max_color_val = 0
        for r in range(len(top_sorted_vert)):
            if r <= l:
                verts = top_sorted_vert[l:r]
                freq = Counter(map(lambda x:colors[x], verts))
                max_color_val = max(max_color_val, max(freq.values()))
                l = r
        verts = top_sorted_vert[l:r]
        freq = Counter(map(lambda x: colors[x], verts))
        return max(max_color_val, max(freq.values()))

sol = Solution()
print(sol.largestPathValue("abaca",[[0,1],[0,2],[2,3],[3,4]]))