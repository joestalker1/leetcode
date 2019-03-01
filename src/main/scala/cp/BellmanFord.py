def bellmanFord(adj):
    dist = [float("inf")] * len(adj)
    dist[1] = 0
    for u in range(1, len(adj)):
        for arr in adj[u]:
            b = arr[0]
            w = arr[1]
            dist[b] = min(dist[b], dist[u] + w)
    return dist

adj = [0] * 6
adj[1] = [[2,1],[4,1]]
adj[2] = [[5,1], [3,1], [1,1]]
adj[3] = [[2,1], [5,1]]
adj[4] = [[1,1]]
adj[5] = [[2,1], [3,1]]

print(bellmanFord(adj))