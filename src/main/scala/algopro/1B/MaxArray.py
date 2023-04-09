def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    max_val = arr[0]
    for i in range(1, n):
        if max_val < arr[i]:
            max_val = arr[i]
    print(max_val)

solve()