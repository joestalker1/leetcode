def dfs(adj_list, u, color):
    color[u] = 1 #gray
    for v in adj_list[u]:
        if color[v] == 1 or color[v] == 0 and dfs(adj_list, v, color):
            return True
    color[u] = 2# black
    return False


def has_cycle(adj_list, n):
    color = [0] * len(n)# white
    for v in range(n):
        if color[v] == 0:
            if dfs(adj_list, v, color):
                return True
    return False



