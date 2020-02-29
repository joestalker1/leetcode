def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

# to calculate multiplicative module inverse
def extendedEclidian(a, b):
    if b == 0:
        d = 1
        x = 1
        y = 0
        return (x, y, d)
    else:
        x1,y1,d = extendedEclidian(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return (x, y, d)

def modInverse(a,m):
    x,y,d = extendedEclidian(a, m)
    return (x % m + m) % m


print(extendedEclidian(5, 12))

print(gcd(40, 10))