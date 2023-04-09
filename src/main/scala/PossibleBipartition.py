from collections import defaultdict

class Solution:
    def possibleBipartition(self, n: int, dislikes) -> bool:
        if n == 0:
            return False
        adj_list = defaultdict(list)
        for a,b in dislikes:
            adj_list[a].append(b)
            adj_list[b].append(a)
        color = [-1] * (n+1)
        for v in range(1, n+1):
            if color[v] != -1:
                continue
            color[v] = 0
            q = [(v,0)]
            while q:
                v,clr = q.pop()
                for nei in adj_list[v]:
                    if color[nei] == clr:
                        return False
                    elif color[nei] == -1:
                        color[nei] = 1 - clr
                        q.append((nei, color[nei]))
        return True