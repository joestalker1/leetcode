def solve(i,j):
    if i == j:
        return 0
    elif i == 1 and i < j:
        return j
    else:
        return i + j - 1


def input_from_con():
    i,j = map(int, input().split())
    print(solve(i,j))


def test():
    assert solve(1,1) == 0
    assert solve(3,4) == 6
    assert solve(1,6) == 6

#test()

input_from_con()