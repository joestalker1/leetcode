def cutRod(arr, n):
    if n <= 0:
        return 0
    profit = [0] * (len(arr) + 1)
    profit[1] = arr[1]
    for i in range(1, n+1):
        for j in range(0, i):
            profit[i] = max(profit[i],arr[j] + profit[i - j - 1])
    return profit[n]


print(cutRod([0, 1,5,8,9,10,17,17,20], 8))