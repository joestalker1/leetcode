def solve():
    x,y = map(float,input().split())
    dist_for_day = x
    eps = 1e-7
    days = 1
    while dist_for_day < y - eps:
        dist_for_day += dist_for_day * 0.7
        days += 1
    print(days)


solve()