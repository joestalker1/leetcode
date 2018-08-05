def comb(n, m):
    if n == 0 or m == 0:
        return 1
    return comb(n-1, m) + comb(n-1,m - 1)

print(comb(5,4))