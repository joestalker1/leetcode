import heapq
from heapq import *

def dijkstra(adj):
    dist = [float("inf")] * len(adj)
    processed = [False] * len(adj)
    dist[1] = 0
    #push weight, vertex
    q = []
    heapq.heappush(q,(0,0))
    while len(q) > 0:
        (_,u) = heapq.heappop(q)
        #vertex is processed already
        if processed[u]:
            continue
        processed[u] = True
        for (v,w) in adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(q, (dist[v], v))



