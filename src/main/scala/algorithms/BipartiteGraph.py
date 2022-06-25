class Solution:
    def isBipartite(self, graph) -> bool:
        color = {}
        for node in range(len(graph)):
            if node in color:
                continue
            st = [node]
            #color the connected component from node
            color[node] = 0
            while st:
                node = st.pop()
                #color its neigbours in different colors
                for nei in graph[node]:
                    if nei not in color:
                        #append to color it neigbours as well.
                        st.append(nei)
                        color[nei] = color[node] ^ 1
                    elif color[nei] == color[node]:
                        return False
        return True
