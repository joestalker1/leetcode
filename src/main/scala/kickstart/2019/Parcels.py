import math


def find_min_dist(d, x, y):
    min_val = math.inf
    for r, c in d:
        min_val = min(min_val, abs(y - r) + abs(x - c))
    return min_val


t = int(input())
for x in range(1, t + 1):
    s = input()
    r,c = map(lambda x: int(x), s.split())
    arr = []
    for i in range(r):
        s = input()
        ln = [int(ch) for ch in list(s)]
        arr.append(ln)
    # check if all cells have delivery
    d = []
    for i in range(r):
        for j in range(c):
            if arr[i][j] == 1:
                d.append([i, j])
    min_dist = [[math.inf] * c for _ in range(r)]

    if len(d) == r * c:
        print("Case #{}: {}".format(x, 0, end='\r\n'))
    else:
        #fill min_dist
        for i in range(r):
            for j in range(c):
                if arr[i][j] == 1:
                    continue
                cur_max = find_min_dist(d, j, i)
                min_dist[i][j] = cur_max

        min_max_val = math.inf
        for i in range(r):
            for j in range(c):
                if arr[i][j] == 1:
                    continue
                #calculate max distance for this
                cur_max = 0
                for i1 in range(r):
                    for j1 in range(c):
                        if arr[i1][j1] == 1 or i1==i and j1 == j:
                            continue
                        cur_dist = abs(i - i1) + abs(j1 - j)
                        if cur_dist < min_dist[i1][j1]:
                            cur_max = max(cur_max, cur_dist)
                        else:
                            cur_max = max(cur_max, min_dist[i1][j1])
                min_max_val = min(min_max_val, cur_max)
        print("Case #{}: {}".format(x, min_max_val, end='\r\n'))
