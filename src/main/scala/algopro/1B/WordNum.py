def solve():
    s = input()
    cnt = 0
    for ch in s:
        if ch == ' ':
            cnt += 1
    print(cnt + 1)


solve()