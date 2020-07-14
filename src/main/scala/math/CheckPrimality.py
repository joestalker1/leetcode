from random import randint


def checkPrime(n):
    i = 1
    count = 0
    while i * i <= n:
        if n % i == 0:
            if i * i == n:
                count += 1  # 2 i are the same
            else:
                count += 2  # i and n/i
        i += 1

    return True if count == 2 else False


def checkPrime2(n):
    k = randint(1, n)
    for i in range(k):
        a = randint(1, n - 1)
        if (a ** (n - 1)) % n != 1:
            return False
    return True


print(checkPrime2(3))
