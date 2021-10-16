import math

def roots(p):
    return (-1 - math.sqrt(8*p+1)) / 2


for p in range(1, 50):
    print(p)
    print(roots(p))