def solve():
    a = int(input())
    b = int(input())
    k = int(input())
    rub = a * k
    coins = b * k
    rub += coins // 100
    return map(str, [rub,coins % 100])

print(' '.join(solve()))