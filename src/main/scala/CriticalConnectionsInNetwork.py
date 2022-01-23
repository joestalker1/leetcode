from collections import defaultdict


class Solution:
    def criticalConnections(self, n: int, connections):
        low = [-1] * n
        disc = [-1] * n
        time = 1
        adj_list = defaultdict(list)
        for s, e in connections:
            adj_list[s].append(e)
            adj_list[e].append(s)

        def find_bridge(u, low, disc, parent, bridge):
            nonlocal time
            low[u] = time
            disc[u] = time
            time += 1
            for v in adj_list[u]:
                if parent == v:
                    continue
                if disc[v] == -1:
                    # call find_bridge for child
                    find_bridge(v, low, disc, u, bridge)
                    # update min times for subtree rooted u
                    low[u] = min(low[u], low[v])
                    # check if no back edge from subtree rooted v
                    if low[v] > disc[u]:
                        bridge.append([u, v])
                else:
                    low[u] = min(low[u], disc[v])

        bridge = []
        for v in range(n):
            if disc[v] == -1:
                find_bridge(v, low, disc, v, bridge)
        return bridge