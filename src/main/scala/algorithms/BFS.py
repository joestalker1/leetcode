def bfs(adj, s):
    q = list()
    dist = [0] * len(adj)
    q.append(s)
    visited = set()
    visited.add(s)
    while len(q) > 0:
        s = q.pop()
        for u in adj[s]:
            if u in visited:
                continue
            q.append(u)
            dist[u] = dist[s] + 1
            visited.add(u)
    return dist

adj = [0] * 6
adj[1] = [4,2]
adj[2] = [5,3,1]
adj[3] = [2, 5]
adj[4] = [1]
adj[5] = [2, 3]
visited = set()
dist = bfs(adj, 1)
[print(dist[i]) for i in range(len(dist))]