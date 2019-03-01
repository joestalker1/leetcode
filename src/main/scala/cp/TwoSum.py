def twoSum(arr, x):
    if not arr:
        return None
    sarr = sorted(arr)
    left = 0
    right = len(arr) - 1

    while left <= right:
        s1 = sarr[left] + sarr[right]
        if s1 == x:
            return [sarr[left], sarr[right]]
        if s1 < x:
            left += 1
        else:
            right -= 1
    return None


print(twoSum([1,4,5,6,7,9,9,10], 12))


