t = int(input())
for _ in range(t):
    n = int(input())
    if n < 2:
        print('composite')
        continue

    from random import randint

    k = 3
    is_prime = True
    for i in range(k):
        a = randint(1, n - 1)
        if (a ** (n-1)) % n != 1:
            is_prime = False
            break
    if is_prime:
        print('prime')
    else:
        print('composite')