
def dijkstra(adj):
    dist = [float("inf")] * len(adj)
    processed = [False] * len(adj)
    dist[1] = 0
    q = [{0,1}] # need binary heap impl
    while len(q) > 0:
        arr = q.pop()
        a = arr[1]
        if processed[a]:
            continue
        processed[a] = True
        for u in adj[a]:
            b = u[0]
            w = u[1]
            if dist[a] + w < dist[b]:
                dist[b] = dist[a] + w
                q.append([dist[b], b])



