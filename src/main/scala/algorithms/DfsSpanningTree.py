#1 is black, 2 is gray, 3 is white
def find_cycle(u, dfs_num, dfs_parent, adj_list):
    dfs_num[u] = 2
    for v in adj_list[u]:
        if dfs_num[v] == 3:
            dfs_parent[v] = u
            find_cycle(v, dfs_num, dfs_parent, adj_list)
        elif dfs_num[v] == 2:
            if v == dfs_parent[u]:
                print('bidirectional')
            else:
                print('cycle {} {}'.format(u, v))
        elif dfs_parent[v] == 0:
            print('forward/cross edge {} {}'.format(u, v))
    dfs_num[u] = 1

#set up all dfs_num to 3


