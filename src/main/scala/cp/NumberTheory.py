#Golbach conjecture
#n = a + b #if n is even then a and b are primes
#Twin prime conjecture
# (p, p+2) are a lot of pairs where p and p + 3 are primes
def prime(n):
    if n < 2:
        return False
    x = 2
    while x*x <= n:
        if n % x == 0:
            return False
        x += 1
    return True

def factors(n):
    facs = []
    x = 2
    while x*x <= n:
        while n % x == 0:
            facs.append(x)
            n /= x
        x += 1
    if n != 1:
        facs.append(int(n))
    return facs

def sieveOfEratosthenes(n):
    if n < 2:
        return n
    sieve = [0] * (n + 1)
    for x in range(2, n+1):
        if sieve[x]:
            continue
        a = 2 * x
        while a <= n:
            sieve[a] = x
            a += x
    return sieve

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    return (a * b) / gcd(a, b)

def mod(x, n):
    if n == 0:
        return 1
    u = mod(x, n // 2)
    u *= u
    if n % 2 == 1:
        u *= x
    return u

def modpow(x, n, m):
    if n == 0:
        return 1 % m
    u = modpow(x, n // 2, m)
    u = (u * u) % m
    if n % 2 == 1:
        u = (u * x) % m
    return u

def phi(n):
    facts = set(factors(n))
    res = n
    for a in facts:
        res = res - res // a
    return res

print(phi(10))


# print((3 ** 6) % 7)
#if m is prime inv of x = x ^ (m - 2)
#print(mod(2, 10))

class Diophantine_equation:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.d = 0

    def calc(self, a, b):
        if b == 0:
            self.x = 1
            self.y = 0
            self.d = a
            return
        self.calc(b, a % b)
        x1 = self.y
        y1 = self.x - (a // b) * self.y
        self.x = x1
        self.y = y1

de = Diophantine_equation()
de.calc(25, 18)

#wilson (n-1)! mod n = n-1 then n is prime
def euler_totient(n):
    return 0 # number comprime numbers to n