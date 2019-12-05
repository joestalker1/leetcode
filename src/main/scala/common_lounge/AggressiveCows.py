t = int(input())

def can_place(x, cows, dist):
    i = 1
    last = 0
    cows -= 1
    while cows > 0 and i < len(x):
        if x[i] - x[last] >= dist:
            last = i
            cows -= 1
        i += 1
    return cows == 0

for i in range(t):
    s = input(' ')
    n,c = s.split()
    n = int(n) # stall number
    c = int(c) # cow number
    x = []
    for _ in range(n):
        xi = input()
        x.append(int(xi))
    x.sort()
    lo = 0
    hi = x[-1]
    max_dist = 0
    while lo < hi:
        dist = lo + (hi - lo) // 2
        if can_place(x, c, dist):
            max_dist = max(max_dist, dist)
            lo = dist + 1
        else:
            hi = dist
    print(max_dist)





