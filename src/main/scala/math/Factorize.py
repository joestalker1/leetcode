def factorize(n):
    i = 2
    res = []
    while i * i <= n:
        while n % i == 0:
            n = n // i
            res.append(i)
        i += 1
    if n != 1:
        res.append(n)  # append last factor
    return res


def factorize2(n):
    minPrime = [0] * (n + 1)
    i = 2
    while i * i <= n:
        if minPrime[i] == 0:
            j = i * i
            while j <= n:
                minPrime[j] = i
                j += i
        i += 1
    for i in range(n + 1):
        if minPrime[i] == 0:
            minPrime[i] = i
    i = n
    res = []
    while i != 1:
        res.append(minPrime[i])
        i = i // minPrime[i]
    return res


print(factorize2(50))









