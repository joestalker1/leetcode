def solve():
    s = input()
    l = 0
    r = len(s) - 1
    while l < r:
        if s[l] != s[r]:
            print('no')
            return
        l += 1
        r -= 1
    print('yes')


solve()
