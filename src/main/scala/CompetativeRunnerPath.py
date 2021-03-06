from collections import defaultdict

def helper(v, visited, stack, edges):
    visited[v] = True

    for neighbor, _ in edges[v]:
        if not visited[neighbor]:
            helper(neighbor, visited, stack, edges)

    stack.append(v)

def toposort(edges, num_vertices):
    visited = [False for _ in range(num_vertices)]
    stack = []

    for v in range(num_vertices):
        if not visited[v]:
            helper(v, visited, stack, edges)

    return stack

def get_distances(edges, stack):
    dist = [float('inf') for _ in range(len(stack))]
    dist[0] = 0

    while stack:
        curr = stack.pop()

        for neighbor, distance in edges[curr]:
            if dist[neighbor] > dist[curr] + distance:
                dist[neighbor] = dist[curr] + distance

    return dist[1:]

#main entry
def shortest_route(elevations, paths):
    uphill_edges = defaultdict(list)
    downhill_edges = defaultdict(list)
    all_edges = defaultdict(list)

    for (start, end), distance in paths.items():
        # split on uphil,downhill routes
        all_edges[start].append((end, distance))
        if elevations[start] < elevations[end]:
            uphill_edges[start].append((end, distance))
        else:
            downhill_edges[end].append((start, distance))

    num_vertices = len(all_edges.keys())
    # get nodes in topological sort order
    stack = toposort(all_edges, num_vertices)
    #calculate min distance for topological sort order in uphill
    uphill_distances = get_distances(uphill_edges, list(stack))
    downhill_distances = get_distances(downhill_edges, list(stack))

    return min(x + y for x, y in zip(uphill_distances, downhill_distances))


elevations = {0: 5, 1: 25, 2: 15, 3: 20, 4: 10}
paths = {
    (0, 1): 10,
    (0, 2): 8,
    (0, 3): 15,
    (1, 3): 12,
    (2, 4): 10,
    (3, 4): 5,
    (3, 0): 17,
    (4, 0): 10
}

print(shortest_route(elevations, paths))
