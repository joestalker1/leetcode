def solve(k,n):
    page = (n-1) // k + 1
    line = (n - 1) % k + 1
    return [page, line]


def input_from_con():
    k, n = map(int, input().split())
    page,line = solve(k,n)
    print('{} {}'.format(page, line))

def test_solve():
    solve(50,1) == [1,1], 'test1'
    solve(20, 25) == [2,5], 'test2'
    solve(15,45) == [3,13], 'test3'

#test_solve()
input_from_con()
