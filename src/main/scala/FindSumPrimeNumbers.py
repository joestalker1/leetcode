def primesum(n):
    for i in range(2, n):
        if is_prime(i) and is_prime(n - i):
            return i, n - i


def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True


print(primesum(6))
