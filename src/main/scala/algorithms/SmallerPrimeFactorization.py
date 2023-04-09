import math

# O(nlog log n)
def sieve(n):
    spf = [0] * (n+1)
    spf[1] = 1
    for i in range(2,n + 1):
        spf[i] = i
    for i in range(2, n +1,2):
        spf[i] = 2
    for i in range(3, int(math.sqrt(n)) + 1):
        if spf[i] == i:
            for j in range(i * i, n + 1,i):
                if spf[j] == j:
                    spf[j] = i
    return spf


def factorize(n):
    spf = sieve(n)
    fact = []
    while n > 1:
        fact.append(spf[n])
        n = n // spf[n]
    return fact

print(factorize(56))