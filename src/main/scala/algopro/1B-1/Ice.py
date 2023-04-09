def solve(k):
    if k >= 5 or k == 3:
        return 'YES'
    return 'NO'


def input_from_con():
    k = int(input())
    print(solve(k))


def test():
    assert solve(3) == 'YES'
    assert solve(5) == 'YES'
    assert solve(8) == 'YES'
    assert solve(11) == 'YES'
    assert solve(1) == 'NO'
    assert solve(4) == 'NO'

#test()

input_from_con()