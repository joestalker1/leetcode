import math

def  findNthRootOfM(n, m):
    err = 1 / 10**8
    diff = math.inf
    xk = 2
    while diff > err:
        xk1 = (math.pow(xk, n) * (n-1) + m) / (n * math.pow(xk, n - 1))
        diff = abs(xk - xk1)
        xk = xk1
    return xk


print(findNthRootOfM(3,27))
