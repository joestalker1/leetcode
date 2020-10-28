import heapq


def min_spanning_tree(pipes):
    # cost, A -> B
    heap = [(0, ('plant', 'plant'))]
    costs = {}
    prev = {}

    seen = set()
    # all vertices
    vertices = pipes.keys()

    while len(seen) != len(vertices):
        cost, edge = heapq.heappop(heap)
        u, v = edge

        if v not in seen:
            # if edges cost is less then in map
            if cost < costs.get(v, float('inf')):
                costs[v] = cost
                # store it to restore path later
                prev[v] = u
            # add neighbours to min-heap
            for neighbor, cost in pipes[v].items():
                heapq.heappush(heap, (cost, (v, neighbor)))

            seen.add(v)
    # create adj_list
    path = {v: [] for v in vertices}
    for u, v in prev.items():
        path[v].append(u)
    # return adj_list and total cost
    return path, sum(costs.values())


print(min_spanning_tree({
    'plant': {'A': 1, 'B': 5, 'C': 20},
    'A': {'C': 15},
    'B': {'C': 10},
    'C': {}
}))
