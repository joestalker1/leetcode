def solve(m,n,k):
    if k < m * n and (k % n == 0 or k % m == 0):
        return 'YES'
    else:
        return 'NO'


def input_from_con():
    m = int(input())
    n = int(input())
    k = int(input())
    print(solve(m,n,k))


def test():
    assert solve(3,2,4) == 'YES'
    assert solve(3,2,1) == 'NO'
    assert solve(2, 2, 4) == 'NO'

test()

input_from_con()