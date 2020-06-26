def checkPrime(n):
    i = 1
    count = 0
    while i*i <= n:
        if n % i == 0:
            if i*i == n:
                count += 1 # 2 i are the same
            else:
                count += 2 # i and n/i
        i += 1

    return True if count == 2 else False


print(checkPrime(7))