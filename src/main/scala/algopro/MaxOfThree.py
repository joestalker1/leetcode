def solve():
    a = int(input())
    b = int(input())
    c = int(input())
    max_ab = a
    if max_ab < b:
        max_ab = b
    return c if c > max_ab else max_ab

print(solve())
