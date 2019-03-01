from collections import defaultdict
from math import log

class FunctionalGraph:
    def __init__(self, n):
        self.graph = defaultdict(list)
        self.n = n
        self.vertices = set()

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.vertices.add(u)
        self.vertices.add(v)

    def succ(self, x, k = 1):
        next = x
        for i in range(k):
            next = self.graph[next][0]
        return next

    def preprocess(self, steps):
        self.prep = [0] * self.n
        for i in range(self.n):
            self.prep[i] = {}
        for x in self.vertices:
            a = 1
            while a <= steps:
                self.prep[x][a] = self.succ(x, a)
                a = a << 1

    def successor(self, x, k):
        log2 = int(log(k, 2))
        suc = x
        while k > 0:
            b = 2 ** log2
            suc = self.prep[suc][b]
            k -= b
            if k > 0:
                log2 = int(log(k, 2))
        return suc

    def cycle(self, x = 1):
        return self.cycle_(x) is not None

    def cycle_(self, x):
        a = self.succ(x)
        b = self.succ(self.succ(x))
        k = self.n
        while a != b and k > 0:
            a = self.succ(a)
            b = self.succ(self.succ(b))
            k -= 1
        return a if a == b else None

    def firstCycleNode(self, x):
        a = self.cycle_(x)
        if not a:
            return None
        b = a
        a = x
        while a != b:
            a = self.succ(a)
            b = self.succ(b)
        return a

    def cycleLen(self, x):
        a = self.firstCycleNode(x)
        if not a:
            return 0
        b = self.succ(a)
        l = 0
        while a != b:
            b = self.succ(b)
            l += 1
        return l









# Class to represent a graph
class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)  # dictionary containing adjacency List
        self.V = vertices  # No. of vertices

    # O(n^2)
    def predecessors(self, x):
        nodes = []
        for i in range(self.V):
            for j in self.graph[i]:
                if j == x:
                    nodes.append(i)
                    break
        return nodes

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

        # A recursive function used by topologicalSort

    def dfs(self, v, visited, stack):

        # Mark the current node as visited.
        visited[v] = True

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if not visited[i]:
                self.dfs(i, visited, stack)

        # Push current vertex to stack which stores result
        stack.insert(0, v)

        # The function to do Topological Sort. It uses recursive

    # topologicalSortUtil()
    def topologicalSort(self):
        # Mark all the vertices as not visited
        visited = [False] * self.V
        stack = []

        # Call the recursive helper function to store Topological
        # Sort starting from all vertices one by one
        for i in range(self.V):
            if visited[i] == False:
                self.dfs(i, visited, stack)

                # Print contents of the stack
        print(stack)
        return stack


def count_of_path(g):
    nodes = g.topologicalSort()
    path = [0] * len(nodes)
    nodes = nodes[:-1]
    path[nodes[len(nodes) - 1]] = 1
    for i in range(len(nodes) - 1, -1, -1):
        n = nodes[i]
        for child in g.graph[n]:
            path[n] += path[child]
    i = 1
    j = len(path) - 1
    while i < j:
        path[i], path[j] = path[j], path[i]
        i += 1
        j -= 1
    return path


def min_number_edges_in_path(g):
    nodes = g.topologicalSort()
    min_num = [0] * len(nodes)
    nodes = nodes[:-1]
    min_num[nodes[len(nodes) - 1]] = 1
    for i in range(len(nodes) - 1, -1, -1):
        n = nodes[i]
        mina = float("inf")
        for child in g.graph[n]:
            if min_num[child] < mina:
                mina = min_num[child]
        if mina < float("inf"):
            min_num[n] = mina + 1
    return min(min_num[1:])


def max_number_edges_in_path(g):
    nodes = g.topologicalSort()
    max_num = [0] * len(nodes)
    nodes = nodes[:-1]
    max_num[nodes[len(nodes) - 1]] = 1
    for i in range(len(nodes) - 1, -1, -1):
        n = nodes[i]
        maxa = 0
        for child in g.graph[n]:
            if max_num[child] > maxa:
                maxa = max_num[child]
        max_num[n] = maxa + 1
    return max(max_num)


# g = Graph(7)
# g.addEdge(1, 2)
# g.addEdge(1, 4)
# g.addEdge(2, 3)
# g.addEdge(3, 6)
# g.addEdge(4, 5)
# g.addEdge(5, 2)
# g.addEdge(5, 3)
# print(max_number_edges_in_path(g))

fg = FunctionalGraph(10)
fg.addEdge(9, 3)
fg.addEdge(1, 3)
fg.addEdge(7, 1)
fg.addEdge(3, 7)

fg.addEdge(4, 6)
fg.addEdge(8, 6)
fg.addEdge(2, 5)
fg.addEdge(5, 2)
fg.addEdge(6, 2)
#fg.preprocess(11)
print(fg.firstCycleNode(4))
print(fg.cycleLen(4))
# print(shortest_path(g))
# print(longest_path(g))
