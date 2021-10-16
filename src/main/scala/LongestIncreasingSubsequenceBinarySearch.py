import bisect
import math

def longest_increasing_subsequence_length(nums):
    n = len(nums)
    dp = [math.inf] * (n + 1)
    #store nums[i] at witch subsequence [0:i] breaks
    dp[0] = -math.inf
    for i in range(n):
        #search dp[i] <= nums[i]
        j = bisect.bisect_left(dp, nums[i])
        if dp[j-1] < nums[i] and nums[i] < dp[j]:
            #update at leftmost dp
            dp[j] = nums[i]
    j = 0
    for i in range(n + 1):
        if dp[i] < math.inf:
            #j is length off
            j = i
    return j

print(longest_increasing_subsequence_length([10, 9, 2, 5, 3, 7, 101, 18]))