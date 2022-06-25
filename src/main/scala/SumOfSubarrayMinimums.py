class Solution:
    def sumSubarrayMins(self, arr) -> int:
        stack = []
        ans = 0
        arr = [float('-inf'), *arr, float('-inf')]
        for i, num in enumerate(arr):
            #if num is new minimum?
            while stack and arr[stack[-1]] > num:
                j = stack.pop()
                #arr[j] is min of right array [i,j] and left of [stack[-1], j]
                ans += arr[j] * (i - j) * (j - stack[-1])
            stack.append(i)
        return ans % (10 ** 9 + 7)