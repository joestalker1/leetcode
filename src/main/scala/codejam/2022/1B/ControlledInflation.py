def solve():
    t = int(input())
    for i in range(1, t+1):
        n,p = list(map(int, input().split()))
        x = []
        for _ in range(n):
            arr = list(map(int, input().split()))
            arr.sort()
            x.append(arr)

        pr = x[0][0]
        for k in range(n):
            for j in range(1,p):
                pr += abs(x[k][j] - x[k][j-1])
            if k > 0:
                pr += abs(x[k][-1] - x[k-1][-1])
        print('Case #{}: {}'.format(i, pr))

solve()
#4999999996
#3999999997