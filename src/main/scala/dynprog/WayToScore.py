def wayToScore(n):
    arr = [0] * (n + 1)
    arr[0] = 1
    for i in range(1, n + 1):
        if i - 3 >= 0:
            arr[i] += arr[i-3]
        if i - 5 >= 0:
            arr[i] += arr[i - 5]
        if i - 10 >= 0:
            arr[i] += arr[i-10]
    return arr[n]


print(wayToScore(13))
