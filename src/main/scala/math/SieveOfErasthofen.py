def sieveLR(l, r):
    isPrime = [1] * (r - l + 1)
    i = 2
    while i * i <= r:
        j = max(i * i, (l + i - 1) // i * i)
        while j <= r:
            isPrime[j - l] = 0
            j += i
        i += 1

    i = max(l, 2)
    while i <= r:
        if isPrime[i - l] == 1:
            print('prime {}'.format(i))
        i += 1


sieveLR(15, 25)
