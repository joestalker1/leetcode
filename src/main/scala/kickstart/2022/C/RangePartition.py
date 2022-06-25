def get_extended(a, b):
    if a == 0:
        return b,0,1
    gcd,x1,y1 = get_extended(b%a, a)
    x = y1 - (b//a)*x1
    y = x1
    return gcd,x,y

def solve():
    t = int(input().strip())
    for i in range(1, t+1):
        n,a,b = map(int, input().split())
        gcd,s1,s2 = get_extended(b,a)
        sumn = n*(n + 1) // 2
        if s1 + s2 > sumn or s1 >= n or s2 >= n or s1 < 0 or s2 < 0:
            print('Case #{}: IMPOSSIBLE'.format(i))
        else:
            if s1 % 2 == 0:
                x1 = 1
                x2 = s1 - x1
            else:
                x1 = 2
                x2 = s1 - x1
            print('Case #{} POSSIBLE'.format(i))
            print(2)
            print('{} {}'.format(x1, x2))

solve()
