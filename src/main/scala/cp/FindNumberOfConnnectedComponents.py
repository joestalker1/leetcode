class ComponentGraph:
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

    def components(self):
        visited = [False] * self.n

        def dfs(v):
            visited[v] = True
            if v not in self.edges:
                return
            for k in self.edges[v]:
                if not visited[k]:
                    dfs(k)
        count = 0
        for i in range(self.n):
            if not visited[i]:
                dfs(i)
                count += 1
        return count




g = ComponentGraph(5)
g.add(1, 0)
g.add(2, 3)
g.add(3, 4)
print(g.components())






