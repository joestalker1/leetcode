def subArraySum(arr, sum):
    j = 0
    cur_sum = 0
    for i in range(len(arr)):
        cur_sum += arr[i]
        if cur_sum == sum:
            return [i,j]
        while cur_sum > sum and j <= i:
            cur_sum -= arr[j]
            j += 1
            if cur_sum == sum:
                return [j, i]
    return [-1,-1]
print(subArraySum([1, 4, 0, 0, 3, 10, 5], 7))
print(subArraySum([1, 4, 20, 3, 10, 5], 33))


