class Solution:
    def catMouseGame(self, graph):
        if not graph:
            return 0
        mouse = 1
        cat = 2
        mouse_seen = {mouse}
        cat_seen = {cat}
        q = [[mouse, 1],[cat,2]]
        while q:
            p,n = q.pop(0)
            if n == 2:
                if p == mouse:
                    return 2
                possible = set(graph[q[0][0]])
                possible.discard(mouse)
                found = False
                for nei in graph[p]:
                    if nei not in cat_seen and nei in possible and nei != 0:
                        q.append([nei,2])
                        cat_seen.add(nei)
                        found = True
                        break
                if not found:
                    for nei in graph[p]:
                        if nei not in cat_seen and nei != 0:
                            q.append([nei, 2])
                            cat_seen.add(nei)
                            found = True
                            break
                if not found:
                    return 0
                cat = p
            if n == 1:
                if p == 0:
                    return 1
                found = False
                forbidden = set(graph[q[0][0]])
                forbidden.discard(cat)
                for nei in graph[p]:
                    if nei not in mouse_seen and nei == 0:
                        q.append([nei, 1])
                        mouse_seen.add(nei)
                        found = True
                        break
                if not found:
                    for nei in graph[p]:
                        if nei not in mouse_seen and nei not in forbidden:
                            q.append([nei, 1])
                            mouse_seen.add(nei)
                            found = True
                            break
                if not found:
                    return 0
                mouse = p
        return 0


sol = Solution()
print(sol.catMouseGame([[3,4],[3,5],[3,6],[0,1,2],[0,5,6],[1,4],[2,4]]))#0
print(sol.catMouseGame([[2,3],[3,4],[0,4],[0,1],[1,2]]))#1
print(sol.catMouseGame([[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]]))
