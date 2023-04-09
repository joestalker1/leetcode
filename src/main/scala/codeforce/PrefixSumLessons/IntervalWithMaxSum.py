import math

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    max_left = 0
    max_right = 0
    max_sum = arr[0]
    cur_sum = arr[0]
    l = 0
    r = 0
    for i in range(1,len(arr)):
        if cur_sum + arr[i] > arr[i]:
            cur_sum += arr[i]
            r = i
        else:
            l = r = i
            cur_sum = arr[i]

        if cur_sum > max_sum:
            max_left,max_right = l,r
            max_sum = cur_sum
    print('{} {} {}'.format(max_left + 1, max_right + 1,max_sum))


solve()