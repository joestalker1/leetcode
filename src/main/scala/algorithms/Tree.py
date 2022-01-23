def countNodes(adj, s, p, count):
    count[s] = 1
    for u in adj[s]:
        if u == p:
            continue
        countNodes(adj, u, s, count)
        count[s] += count[u]

arr = [[1,2],
       [],
       [3,4],
       [],
       []]

count = [0] * 5
#countNodes(adj, 0, -1, count)

def toLeaf(adj, x):
    n = len(adj)
    count = [0] * n
    countNodes(adj, x, -1, count)
    max_count = 0
    for u in adj[x]:
        if count[u] > max_count:
            max_count = count[u]
    return max_count

def maxLength(adj, x):
    max_leaf = [0] * len(adj[x])
    i = 0
    for u in adj[x]:
        max_leaf[i] = toLeaf(adj, u)
        i += 1
    max1 = 0
    max2 = 0
    for a in max_leaf:
        if a > max1:
            max2 = max1
            max1 = a
        elif a > max2:
            max2 = a
    max1 += 1
    max2 += 1
    return max1 + max2


def diameter(adj):
    return maxLength(adj, 1)

arr = [
    [],
    [2,3,4],
    [5,6],
    [],
    [7],
    [],
    [],
    []
  ]

print(diameter(arr))





