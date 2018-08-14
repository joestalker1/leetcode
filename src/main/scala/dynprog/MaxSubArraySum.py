#Kadane algoritm
def maxSubArraySum(arr):
    if not arr:
        return 0
    max_sum = 0
    cur_sum = 0
    for i in range(len(arr)):
        cur_sum += arr[i]
        if cur_sum < 0:
            cur_sum = 0
        max_sum = max(cur_sum, max_sum)
    return max_sum

print(maxSubArraySum([-2,-3,4,-1,-2,1,5,-3]))