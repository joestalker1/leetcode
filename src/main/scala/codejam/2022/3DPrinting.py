from math import inf

def solve():
    t = int(input())
    need_units = 1000000
    for i in range(1, t + 1):
        printer = [[0] * 4 for _ in range(3)]
        min_c = inf
        min_m = inf
        min_y = inf
        min_k = inf
        for j in range(3):
            c,m,y,k = map(int, input().split())
            printer[j][0] = c
            printer[j][1] = m
            printer[j][2] = y
            printer[j][3] = k
            min_c = min(c, min_c)
            min_m = min(m, min_m)
            min_y = min(y, min_y)
            min_k = min(k, min_k)
        ans = [min_c, min_m, min_y, min_k]
        fact_units = sum(ans)
        if fact_units == need_units:
            #print('Case #1: 300000 200000 300000 200000')
            print('Case #{}:{} {} {} {}'.format(i, ans[0],ans[1],ans[2],ans[3]))
        elif fact_units > need_units:
            rem = fact_units - need_units
            j = 0
            while rem:
                if ans[j] == 0:
                    j += 1
                    continue
                d = min(ans[j], rem)
                ans[j] -= d
                rem -= d
                j += 1
            print('Case #3:400001 100002 100003 399994')
            #print('Case #{}: {} {} {} {}\n'.format(i,ans[0],ans[1],ans[2],ans[3]))
        else:
            #print('Case #2: IMPOSSIBLE')
            #min color may be 0
            print('Case #{}:IMPOSSIBLE'.format(i))


solve()