def find_max_subarr(arr):
    if not arr:
        return 0
    max_val = 0
    sum = 0
    for i in range(len(arr)):
        sum = max(arr[i], sum + arr[i])
        max_val = max(max_val, sum)
    return max_val


print(find_max_subarr([-1,2,3,-2,5]))
print(find_max_subarr([2,-3,4,9,0]))