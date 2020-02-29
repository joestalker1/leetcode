name = input()  # Reading input from STDIN
a, b, c, m = name.split(' ')
a = int(a)
b = int(b)
c = int(c)
m = int(m)


def mod_exponentiation(a, n, m):
    if n == 0:
        return 1
    if n % 2 == 0:
        return mod_exponentiation((a * a) % m, n // 2, m)
    else:
        return (a * mod_exponentiation((a * a) % m, (n - 1) // 2, m)) % m


def extended_eclidian(a, b):
    if b == 0:
        d = 1
        x = 1
        y = 0
        return (x, y, d)
    else:
        x1, y1, d = extended_eclidian(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return (x, y, d)


def multiplicative_module_inverse(a, m):
    x, y, d = extended_eclidian(a, m)
    # x is multiplicative module inverse
    return (x % m + m) % m


def exp(a, b, c, m):
    a1 = mod_exponentiation(a, b, m)
    a2 = multiplicative_module_inverse(c, m)
    return (a1 * a2) % m


res = exp(a, b, c, m)

print('Hi, %s.' % res)
