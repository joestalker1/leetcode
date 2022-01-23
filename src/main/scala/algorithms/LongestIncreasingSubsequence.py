def longIncrSub(arr):
    if not len(arr):
        return 0
    length = [0] * len(arr)
    for k in range(0, len(arr)):
        #min length
        length[k] = 1
        #found arr itmes being less then arr[k]
        for i in range(0, k):
            if arr[i] < arr[k]:
                length[k] = max(length[k], 1 + length[i])
    return length[len(arr) - 1]


arr = [6, 2, 5, 1, 7, 4, 8, 3]
print(longIncrSub(arr))
