def find_diff_arr(arr):
    n = len(arr)
    b = [0]* (n-1)
    for i in range(n-1):
        b[i] = arr[i+1] - arr[i]
    return b

def find_prefix_sum(arr):
    n = len(arr)
    b = [0] * (n+1)
    for i in range(n):
        b[i + 1] = b[i] + arr[i]
    return b

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    arr.insert(0, 0)
    arr.insert(0, 0)
    diff = find_diff_arr(arr)
    diff = find_diff_arr(diff)
    q = int(input())
    for _ in range(q):
        l,r,d = list(map(int, input().split()))
        l -= 1
        #consider [l, r)
        diff[l] += d
        #r -= 1
        if r < len(diff):
            diff[r] -= (r - l + 1) * d
        if r + 1 < len(diff):
            diff[r+1] += (r - l) * d
        # if r - 1 < len(diff):
        #     diff[r-1] += d2
    new_arr = find_prefix_sum(diff)
    new_arr = find_prefix_sum(new_arr)
    new_arr.pop(0)
    new_arr.pop(0)
    print(*new_arr)


solve()