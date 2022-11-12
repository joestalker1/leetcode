import math

class Solution:
    def maxNumOfSubstrings(self, s):
        if not s:
            return []
        #use kasarju algorithm to find SCC
        min_index = [math.inf] * 26
        max_index = [-math.inf] * 26
        exists = [False] * 26
        # consider every substring from 0 to i by holding the char frequency
        pr_sum = [[0] * 26 for _ in range(len(s) + 1)]

        def code(ch):
            return ord(ch) - ord('a')
        #st contains topological sorted chars
        def topol_sort(v, graph, st, visited):
            if visited[v]:
                return
            visited[v] = 1
            #iterate over all chars
            for j in range(26):
                if graph[v][j] and visited[j] == 0:
                    topol_sort(j, graph, st, visited)
            st.append(v)

        def dfs(v, graph, batches, batch, degree):
            if batches[v] < 0:
                #assign char to scc id of current component
                batches[v] = batch
                for i in range(26):
                    if graph[i][v]:
                        dfs(i, graph, batches, batch, degree)
            else:
                #if vertex has other scc id, update out degree number of this scc id.
                if batches[v] != batch:
                    degree[batches[v]] += 1

        for i in range(len(s)):
            #make copy the previous row,because string [0:i+1] contains the chars of string [0:i]
            pr_sum[i + 1] = pr_sum[i][::]
            pr_sum[i + 1][code(s[i])] += 1
            #update min index of char
            min_index[code(s[i])] = min(i, min_index[code(s[i])])
            #update max index of char
            max_index[code(s[i])] = max(i, max_index[code(s[i])])
            exists[code(s[i])] = True

        graph = [[0] * 26 for _ in range(26)]
        for c1 in range(26):
            if exists[c1]:
                for c2 in range(26):
                    # if all chars j are only in a substring having char i, we make connection
                    # between i and j
                    # if c2 is in string [min_index[c1]:max_index[c2]], we make connection c1 -> c2
                    if (pr_sum[max_index[c1] + 1][c2] - pr_sum[min_index[c1]][c2]) > 0:
                        graph[c1][c2] = True

        # kosaraju algorithm to find scc
        st = []
        visited = [0] * 26
        for i in range(26):
            if exists[i] and visited[i] == 0:
                topol_sort(i, graph, st, visited)
        batch = 0 # id of each SCC
        batches = [-1] * 26
        degree = [0] * 26 # out-degree of each SCC
        while st:
            v = st.pop()
            if batches[v] < 0:
                dfs(v, graph, batches, batch, degree)
                batch += 1
        res = []
        for i in range(batch - 1, -1, -1):
            #if scc doesn't have any out edges, process it.
            if degree[i] == 0:
                min_v = math.inf
                max_v = -math.inf
                #find outer indices of this component.
                for j in range(26):
                    if batches[j] == i:
                        min_v = min(min_v, min_index[j])
                        max_v = max(max_v, max_index[j])
                res.append(s[min_v:max_v + 1])
        return res