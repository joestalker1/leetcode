t = int(input())
#t test cases
for r in range(1, t + 1):
    #N, K, x1, y1, C, D, E1, E2 and F
    s = input()
    s = s.split()
    arg = list(map(lambda x: int(x), s))
    n,k,x1,y1,c,d,e1,e2,f = arg
    mod = 10 ** 9 + 7
    A = [0] * n
    A[0] = (x1 + y1) % f

    #xi = ( C × xi-1 + D × yi-1 + E1 ) modulo F.
    # yi = ( D × xi-1 + C × yi-1 + E2 ) modulo F
    # Ai = ( xi + yi ) modulo F
    for i in range(1, n):
        x = (c * x1 + d * y1 + e1) % f
        y = (d * x1 + c * y1 + e2) % f
        x1 = x
        y1 = y
        A[i] = (x1 + y1) % f
    # result = 0
    # GP_sum = K  # Handling p = 1 case separately.
    # mod = 1000000007
    # for (x in 1 to N) {
    # if x != 1
    # GP_sum = GP_sum + (pow(x, K+1)-1) * pow(x-1, mod-2)  # Multipyting by inverse modulo of x-1.
    # GP_sum %= mod
    #
    # result = result + GP_sum * A[x]
    # result %= mod
    # }
    res = 0
    gp_sum = k
    for i in range(1, n):
        if i != 1:
            gp_sum = gp_sum + (i **(k+1) - 1) * ((i - 1) ** (mod - 2))
            gp_sum %= mod
        res = res + gp_sum * A[i-1]
        res %= mod
    print("Case #{}: {}".format(r, res, end='\r\n'))








