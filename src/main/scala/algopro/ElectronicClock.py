def solve():
    n = int(input())
    hours = (n // 60) % 24
    minutes = n % 60
    return map(str, [hours, minutes])

print(' '.join(solve()))
