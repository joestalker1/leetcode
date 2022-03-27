def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def solve():
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        b = input().strip().split(' ')
        b = [int(b[i]) for i in range(n)]
        a = [0] * n
        #check if b[i-1] and b[i] has gcd,if they don't,return -1
        a[0] = b[0]
        bad = False
        for i in range(1, n):
            g = gcd(b[i-1], b[i])
            if g != b[i]:
                bad = True
                break
            else:
                a[i] = b[i]
        if bad:
            print('-1\n')
        else:
            a = [str(a[i]) for i in range(n)]
            print(' '.join(a))
        print('\n')
solve()