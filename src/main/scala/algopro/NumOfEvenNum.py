def solve():
    cnt = 0
    while True:
        n = int(input())
        if n == 0:
            return cnt
        if n % 2 == 0:
            cnt += 1


print(solve())
