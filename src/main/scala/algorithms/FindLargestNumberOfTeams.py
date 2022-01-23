
class GraphVertex:
    def __init__(self):
        self.edges = []
        self.max_dist = 1
        self.visited = False

def findLargestNumberTeams(g):
    orderedVertices = buildTopologicalOrdering(g)
    return findLongestPath(orderedVertices)

def findLongestPath(orderedVertices):
    max_dist = 0
    while len(orderedVertices) > 0:
        u = orderedVertices.pop(0)
        max_dist = max(max_dist, u.max_dist)
        for v in u.edges:
            v.max_dist = max(v.max_dist, u.max_dist + 1)
    return max_dist

def buildTopologicalOrdering(g):
    orderedVertices = []
    for v in g:
        if not v.visited:
            topologicalSort(g, orderedVertices)
    return orderedVertices

def topologicalSort(cur, orderedVertices):
    cur.visited = True
    for v in cur.edges:
        if not v.visited:
            topologicalSort(v, orderedVertices)
    orderedVertices.insert(0, cur)








