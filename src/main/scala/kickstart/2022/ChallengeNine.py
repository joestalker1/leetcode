import math

def to_int(digits):
    b = map(str, digits)
    return int(''.join(b))

def solve():
    t = int(input())
    for k in range(1, t + 1):
        a = int(input().strip())
        digits = []
        b = a
        while b:
            d = b % 10
            digits.insert(0, d)
            b = b // 10
        s = sum(digits)
        if s % 9 == 0:
            d = 0
        else:
            q = s // 9 + 1
            d = q * 9 - s
        if d == 0 and len(digits) == 1:
            digits.append(0)
        else:
            l = -1
            if d == 0:
                l = 0
            for i in range(len(digits)-1, l, -1):
                if digits[i] <= d:
                    digits.insert(i, d)
                    break
        print('Case #{}: {}\n'.format(k, to_int(digits)))

solve()

