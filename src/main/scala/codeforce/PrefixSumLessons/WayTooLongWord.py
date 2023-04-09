def solve():
    n = int(input())
    for _ in range(n):
        s = input().strip()
        if len(s) <= 10:
            print(s)
        else:
            print('{}{}{}'.format(s[0], len(s) - 2,s[-1]))

solve()