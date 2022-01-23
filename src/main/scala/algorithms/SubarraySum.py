def subArraySum(arr, x):
    if not arr:
        return None
    i1 = 0
    i2 = 0
    s1 = arr[0]
    while i1 < len(arr):
        if s1 == x:
            return [i1, i2]
        if s1 < x:
            i2 += 1
            if i2 < len(arr):
                s1 += arr[i2]
        else:
            s1 -= arr[i1]
            i1 += 1
    return None

print(subArraySum([1,3,2,5,1,1,2,3], 8))