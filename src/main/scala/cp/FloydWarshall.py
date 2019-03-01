def floydWarshal(adj):
    n = len(adj)
    dist = [0] * n
    for i in range(len(dist)):
        dist[i] = [0] * n

    for i in range(0, n):
        for j in range(0, n):
            if i == j:
                continue
            if adj[i][j]:
                dist[i][j] = adj[i][j]
            else:
                dist[i][j] = float("inf")

    for k in range(0, n):
        for i in range(0, n):
            for j in range(0, n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist



