t = int(input())
for x in range(1, t+1):
    s = input()
    n,p = map(lambda x:int(x), s.split())
    s = input()
    skills = list(map(lambda x: int(x), s.split()))
    skills.sort()

    max_skill = [0] * n
    max_skill[0] = skills[0]
    for i in range(1, n):
        max_skill[i] = max(max_skill[i-1],skills[i])
    cur_sum = 0
    res = 10001 * p
    for r in range(n):
        if (r + 1) > p:
            cur_sum -= skills[r-p]
        cur_sum += skills[r]
        if (r + 1) >= p:
            res = min(res, max_skill[r] * p - cur_sum)
        #calculate training cost from l to r
    print("Case #{}: {}".format(x, res, end='\r\n'))



