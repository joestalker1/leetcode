def solve():
    sums = 0
    while True:
        n = int(input())
        if n == 0:
            return sums
        sums += n

print(solve())


