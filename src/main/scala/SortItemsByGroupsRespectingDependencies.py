from collections import defaultdict

class Solution:
    def sortItems(self, n, m, group, beforeItems):
        if not group or not beforeItems:
            return []
        node_graph = defaultdict(list)
        group_graph = defaultdict(list)
        group_to_node = defaultdict(list)

        for node in range(n):
            group_to_node[group[node]].append(node)

        for node,before_items in enumerate(beforeItems):
            for before_item in before_items:
                node_graph[before_item].append(node)
                if group[before_item] != group[node]:
                    group_graph[group[before_item]].append(group[node])

        visited_group = [False] * (m + 1)

        def group_top_sort(g, visited, adj_list, res):
            visited[g + 1] = True
            for neighbour in adj_list[g]:
                if not visited[neighbour + 1]:
                    group_top_sort(neighbour, visited, adj_list, res)
            res.insert(0, g)

        def item_top_sort(node, g, visited, adj_list, res):
            visited[node] = True
            if group[node] == g:
                for neighbour in adj_list[node]:
                    if group[neighbour] != g:
                        continue
                    if not visited[neighbour]:
                        item_top_sort(neighbour, g, visited, adj_list, res)
                res.insert(0, node)

        res_group = []
        for g in range(-1, m):
            if not visited_group[g + 1]:
                group_top_sort(g, visited_group, group_graph, res_group)
        res = []
        visited_item = [False] * n
        for i in range(len(res_group) - 1, -1, -1):
            g = res_group[i]
            for node in group_to_node[g]:
                if not visited_item[node]:
                    item_top_sort(node, g, visited_item, node_graph, res)
        pos_to_node = {node:i for i,node in enumerate(res)}
        #check if all nodes follow to restrictions
        for i,node in enumerate(res):
            for before_item in beforeItems[node]:
                if pos_to_node[before_item] > i:
                    return []
        return res

sol = Solution()
print(sol.sortItems(n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3],[],[4],[]]))#[]
print(sol.sortItems(n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3,6],[],[],[]]))











