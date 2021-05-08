def max_score(scores):
    n = len(scores)
    if n % 2 == 0:
        h = n // 2
    else:
        h = n // 2 + 1

    cur_beauty = 0
    for i in range(h):
        cur_beauty += scores[i]
    max_beauty = cur_beauty
    for r in range(h, n):
        cur_beauty += (-scores[r - h] + scores[r])
        max_beauty = max(max_beauty, cur_beauty)
    return max_beauty

n = int(input())
for i in range(n):
    t = int(input())
    s = input()
    scores = list(map(lambda x: int(x), s))
    print("Case #{}: {}".format(i+1, max_score(scores)), end='\r\n')
