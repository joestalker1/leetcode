def bellmanFord(adj, n):
    dist = [float("inf")] * len(adj)
    dist[1] = 0
    # relax all edges V times, every path can be at most v vertices
    for u in range(1, n+1):
        for (v,w) in adj[u]:
            dist[v] = min(dist[v], dist[u] + w)
    for u in range(1, n + 1):
        for (v,w) in adj[u]:
            if dist[u] + w < dist[w]:
                print(f'Found negative cycle $u -> $v')

    return dist

adj = [0] * 6
adj[1] = [[2,1],[4,1]]
adj[2] = [[5,1], [3,1], [1,1]]
adj[3] = [[2,1], [5,1]]
adj[4] = [[1,1]]
adj[5] = [[2,1], [3,1]]

print(bellmanFord(adj, 5))