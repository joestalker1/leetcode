def minimazeSum(arr):
    if not arr:
        return None

    sorted_arr = sorted(arr)
    mid = len(sorted_arr) // 2
    return sorted_arr[mid]


print(minimazeSum([1,2,9,2,6]))

def minimazeSquareSum(arr):
    if not arr:
        return None
    sum1 = 0
    for a in arr:
        sum1 += a
    return sum1 // len(arr)

print(minimazeSquareSum([1,2,9,2,6]))