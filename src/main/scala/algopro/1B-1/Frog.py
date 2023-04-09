def solve(k,t):
    #switch of either first or second expression.
    p = (t // k) % 2
    return (k - t % k)* p + (t % k) * (p - 1) * (-1) ** (p+1)


def input_from_con():
    #test_solve()
    k,t = map(int, input().split())
    step = solve(k,t)
    print(step)

def test_solve():
    solve(3,1) == 2, 'test1'
    solve(3, 10) == 2, 'test2'
    solve(3,12) == 0, 'test3'

input_from_con()

#
