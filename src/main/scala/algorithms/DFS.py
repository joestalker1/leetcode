def dfs(adj, visited, s):
    if s in visited:
        return
    visited.add(s)
    for u in adj[s]:
        dfs(adj, visited, u)


def connectivity_check(adj):
    visited = set()
    dfs(adj, visited, 1)
    return len(visited) == len(adj) - 1


def find_all_components(adj):
    visited = set()
    c = 0
    for u in range(1, len(adj)):
        if u not in visited:
            dfs(adj, visited, u)
            c += 1
    return c

def bipartiteness_check(adj):
    def dfs(adj, visited, colors, s):
        if s in visited:
            return True
        visited.add(s)
        clr = colors[s]
        if clr == 2:
            clr = 3
        else:
            clr = 2
        for u in adj[s]:
            if colors[s] != 0 and colors[s] == colors[u]:
                return False
            colors[u] = clr
            res = dfs(adj, visited, colors, u)
            if not res:
                return res
        return True
    colors = [0] * len(adj)
    colors[1] = 2
    return dfs(adj, set(), colors, 1)

adj = [0] * 6
adj[1] = [2,4]
adj[2] = [5, 3, 1]
adj[3] = [2, 5]
adj[4] = [1]
adj[5] = [2, 3]

print(bipartiteness_check(adj))
