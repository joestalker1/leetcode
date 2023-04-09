def solve():
    n = int(input())
    return n % 400 == 0 or (n % 4 == 0 and (n % 100) != 0)

is_leap = solve()
print('YES' if is_leap else 'NO')