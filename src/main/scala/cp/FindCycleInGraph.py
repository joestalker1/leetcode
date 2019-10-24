class UndirectedGraph:
    def __init__(self, n):
        self.edges = {}
        self.n = n

    def add(self, v, w):
        list1 = [] if v not in self.edges else self.edges[v]
        list1.append(w)
        self.edges[v] = list1
        list1 = [] if w not in self.edges else self.edges[w]
        list1.append(v)
        self.edges[w] = list1

    def has_cycle(self):
        visited = [False] * self.n

        def dfs(v, parent):
            visited[v] = True
            if v not in self.edges:
                return False
            for k in self.edges[v]:
                if not visited[k]:
                    if dfs(k, v):
                        return True
                elif parent != k:
                    return True
            return False

        for i in range(self.n):
            if not visited[i]:
                if dfs(i, -1):
                    return True
        return False

g = UndirectedGraph(3)
g.add(0, 1)
g.add(1, 2)
g.add(2, 0)
print(g.has_cycle())
