
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
    n,m,k = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    arr.insert(0, 0)
    diff = find_diff_arr(arr)
    q = []
    #input queries
    for _ in range(m):
        l,r,d = list(map(int, input().split()))
        q.append([l-1,r,d])
    cnt = [0] * m
    for _ in range(k):
        x,y = list(map(int, input().split()))
        x -= 1
        cnt[x] += 1
        if y < m:
            cnt[y] -= 1
    for i in range(1, m):
        cnt[i] += cnt[i - 1]
    for i in range(m):
        l,r,d = q[i]
        diff[l] += d * cnt[i]
        if r < len(diff):
            diff[r] -= d * cnt[i]
    new_arr = find_prefix_sum(diff)
    new_arr.pop(0)
    print(*new_arr)


solve()


