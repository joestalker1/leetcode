class Solution:
    def minimumTime(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        #for suffix i:n
        left = [0] * n
        right = [0] * n
        if s[0] == '1':
            left[0] = 1
        for i in range(1, n):
            if s[i] == '1':
                left[i] = min(left[i-1] + 2, i+1)
            else:
                left[i] = left[i-1]
        right[-1] = 1 if s[-1] == '1' else 0
        for i in range(n-2,-1,-1):
            if s[i] == '1':
                right[i] = min(right[i+1] + 2, len(s) - i)
            else:
                right[i] = right[i+1]
        #compare applying either left or right completly
        min_cost = min(left[-1], right[0])
        for i in range(n-1):
            min_cost = min(min_cost, left[i] + right[i+1])
        return min_cost

