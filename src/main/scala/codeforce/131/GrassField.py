def solve():
    t = int(input())
    for i in range(t):
        a,b = map(int, input().split())
        c,d = map(int, input().split())
        arr = [a,b,c,d]
        ones = sum([x for x in arr if x == 1])
        if ones == 0:
            print('0')
        elif ones in [1,2,3]:
            print('1')
        else:
            print('2')


solve()
