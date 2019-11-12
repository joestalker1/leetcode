class Solution:
    def find_max_flow(self, adj, adj_mat):
        p = {}
        s = 0
        t = 0
        max_flow = 0
        while True:
            self.f = 0
            q = []
            dist = {}
            q = [s]
            dist[s] = 0
            while q:
                u = q.pop(0)
                if u == t:
                    break
                for v in adj[u]:
                    if adj_mat[u][v] > 0 and v not in dist:
                        dist[v] = dist[u] + 1
                        q.append(v)
                        p[v] = u
            self.augment_path(p, s, t, float('inf'), adj_mat)
            if self.f == 0:
                break
            max_flow += self.f
        return max_flow

    def augment_path(self, p, s, v, min_edge, adj_mat):
        if v == s:
            self.f = min_edge
            return
        if v in p:
            self.augment_path(p, s, p[v], min(min_edge, adj_mat[p[v]][v]), adj_mat)
            adj_mat[p[v]][v] -= self.f
            adj_mat[v][p[v]] += self.f













