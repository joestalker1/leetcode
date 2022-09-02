# User function Template for python3
from collections import defaultdict


class Solution:

    # Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):

        def dfs(adj, v, vertices,seen):
            if v == V or v in seen:
                return
            vertices.append(v)
            seen.add(v)
            if len(adj) <= v:
                return
            for nei in adj[v]:
                dfs(adj, nei, vertices,seen)

        vertices = []
        dfs(adj, 0, vertices,set())
        return vertices


# {
# Driver Code Starts
if __name__ == '__main__':
    T = int(input())
    while T > 0:
        V, E = map(int, input().split())
        adj = [[] for i in range(V + 1)]
        for i in range(E):
            u, v = map(int, input().split())
            adj[u].append(v)
            adj[v].append(u)
        ob = Solution()
        ans = ob.dfsOfGraph(V, adj)
        for i in range(len(ans)):
            print(ans[i], end=" ")
        print()
        T -= 1
# } Driver Code Ends