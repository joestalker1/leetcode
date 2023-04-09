def solve():
    n = int(input())
    for i in range(2,n+1):
        if n % i == 0:
            return i

print(solve())
