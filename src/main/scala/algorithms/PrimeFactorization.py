
def prime_factorization(max_val):
    v = [0] * max_val
    sp = [0] * max_val
    for i in range(2, max_val, 2):
        sp[i] = 2
    for i in range(3, max_val, 2):
        if v[i] == 0:
            sp[i] = i
            j = i
            while j * i < max_val:
                if v[j*i] == 0:
                    v[j * i] = 1
                    sp[j * i] = i
                j += 2
    return sp


sp = prime_factorization(10**7)
for i in range(50):
    print("{} {}".format(i, sp[i]))
