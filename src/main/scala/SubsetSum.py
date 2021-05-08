import bisect


def generateSubsetSum(arr, n, c):
    res = []
    for i in range(1 << n):
        s = 0
        for j in range(n):
            if i & (1 << j):
                s += arr[j + c]
        res.append(s)
    return res

def subsetsum(arr, target):
    # devide arr by 2 and generate sum for left and right parts
    n = len(arr)
    left = generateSubsetSum(arr, n // 2, 0)
    right = generateSubsetSum(arr, n - n//2, n // 2)
    left.sort()
    #max sum is less then target
    max_sum = 0
    for s in right:
        if s <= target:
            i = bisect.bisect_left(left, target - s)
            if i == len(left) or left[i] != target - s:
                i -= 1
            max_sum = max(max_sum, s + left[i])
    return max_sum


print(subsetsum([45, 34, 4, 12, 5, 2], 42))