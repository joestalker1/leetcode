def pathInGrid(arr):
    if not arr:
        return 0
    n = len(arr)
    sum1 = [0] * n
    for i in range(0, n):
        sum1[i] = [0] * n
    for i in range(1, n):
        for x in range(1, n):
            sum1[i][x] = max(sum1[i][x-1], sum1[i - 1][x]) + arr[i][x]
    return sum1[n-1][n-1]


arr = [ [3,7,9,2,7],
        [9,8,3,5,5],
        [1,7,9,8,5],
        [3,8,6,4,10],
        [6,3,9,7,8]
        ]

print(pathInGrid(arr))

