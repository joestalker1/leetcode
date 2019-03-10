# n choose k = (n-1) choose (k-1) + (n-1) choose k
def n_choose_k(n, k):
    if k == 0 or n == k:
        return 1
    return n_choose_k(n - 1, k - 1) + n_choose_k(n - 1, k)


#print(n_choose_k(5, 3))


# multinomial coefficients
# n! / k1! * k2! *..km! where k1 + k2 + ... km = n
def catalan_num(n):
    return int(1 / (n + 1) * n_choose_k(2 * n, n))


#print('number of binray tree is {}'.format(catalan_num(3)))


# a or b = a + b - a and b
# a or b or c = a + b + c - a and b - a and c - b and c + a and b and c
# a and c and b = a + b + c - a or b - a or c - b or c + a or b or c
import math

def derangements(n):
    if n == 1 or n == 2:
        return n - 1
    return (n - 1) * (derangements(n - 2) + derangements(n - 1))
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def burnside(n, m):
    s = 0
    for i in range(n):
        s += (math.pow(m, gcd(i,n)) / n)
    return s

print(burnside(4, 3))
#print(derangements(3))