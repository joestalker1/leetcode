from collections import defaultdict
#kosarju

# This class represents a directed graph using adjacency list representation
class Graph:
    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = defaultdict(list)  # default dictionary to store graph

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

        # A function used by isSC() to perform DFS

    def dfs(self, v, visited):

        # Mark the current node as visited
        visited[v] = True

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.dfs(i, visited)

        # Function that returns reverse (or transpose) of this graph

    def transpose(self):

        g = Graph(self.V)

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph:
            for j in self.graph[i]:
                g.addEdge(j, i)

        return g

        # The main function that returns true if graph is strongly connected

    def is_strong_connected(self):

        # Step 1: Mark all the vertices as not visited (For first DFS)
        visited = [False] * (self.V)

        # Step 2: Do DFS traversal starting from first vertex.
        self.dfs(0, visited)

        # If DFS traversal doesnt visit all vertices, then return false
        if any(a == False for a in visited):
            return False

        # Step 3: Create a reversed graph
        gr = self.transpose()

        # Step 4: Mark all the vertices as not visited (For second DFS)
        visited = [False] * (self.V)

        # Step 5: Do DFS for reversed graph starting from first vertex.
        # Staring Vertex must be same starting point of first DFS
        gr.dfs(0, visited)

        # If all vertices are not visited in second DFS, then
        # return false
        if any(i == False for i in visited):
            return False

        return True


gr = Graph(4)
gr.addEdge(0, 1)
gr.addEdge(1, 3)
gr.addEdge(3, 2)
gr.addEdge(2, 0)
print(gr.is_strong_connected())


