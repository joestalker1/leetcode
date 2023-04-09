def solve():
    n = int(input())
    is_zero = False
    for _ in range(n):
        a = int(input())
        if a == 0 and not is_zero:
            is_zero = True
    return is_zero

print('YES' if solve() else 'NO')
