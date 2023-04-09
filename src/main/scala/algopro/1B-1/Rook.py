def solve(x1,y1,x2,y2):
    #switch of either first or second expression.
    if x1 == x2 or y1 == y2:
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