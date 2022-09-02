from math import inf

def solve():
    t = int(input())
    for i in range(t):
        n = int(input())
        if n == 1:
            print('1')
            print('1')
            continue
        elif n == 2:
            print('2')
            print('1 2')
        elif n == 3:
            print('3')
            print('1 3 2')
        else:
            res = []
            #build beg
            res.append(1)
            j = 2
            used = set()
            used.add(1)
            while j <= n:
                res.append(j)
                used.add(j)
                j *= 2
            for i in range(3, n + 1):
                if i in used:
                    continue
                j = i
                while j <= n:
                    used.add(j)
                    res.append(j)
                    j *= 2
            print('2')
            print(' '.join(map(str, res)))

solve()



