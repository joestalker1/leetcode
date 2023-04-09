def solve(m,n,k):
    if k % n == 0 or k % m == 0:
        return 'YES'
    else:
        return 'NO'

    #switch of either first or second expression.
    if abs(x1 - x2) == abs(y1-y2):
        return 'YES'
    else:
        return 'NO'


def input_from_con():
    #test_solve()
    x1 = int(input())
    y1 = int(input())
    x2 = int(input())
    y2 = int(input())
    print(solve(x1,y1,x2,y2))


input_from_con()