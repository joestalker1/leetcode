def solve():
    s1 = input()
    if len(s1.split()) > 1:
        x,y = map(float, s1.split())
    else:
        x = float(s1)
        y = float(input())
    dist_for_day = x
    eps = 1e-7
    days = 1
    total_dist = dist_for_day
    while total_dist < y - eps:
        dist_for_day += dist_for_day * 0.7
        total_dist += dist_for_day
        days += 1
    print(days)


solve()
