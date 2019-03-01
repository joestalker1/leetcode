def distance(a, b):
    if not a and not b:
        return 0
    if not a:
        return len(b)
    if not b:
        return len(a)
    n1 = len(a) + 1
    n2 = len(b) + 1
    dist = [0] * n1
    for i in range(0, n1):
        dist[i] = [0] * n2
    for i in range(1, n1):
        dist[i][0] = i
    for i in range(1, n2):
        dist[0][i] = i

    for i in range(1, n1):
        for j in range(1, n2):
            if a[i-1] == b[j-1]:
                c = 0
            else:
                c = 1
            dist[i][j] = min(dist[i][j-1]+1, dist[i-1][j] + 1,dist[i-1][j-1] + c)
    return dist[n1-1][n2-1]

print(distance("LOVE","MOVIE"))

