class Solution:
    def maxValue(self, n: int, index: int, maxSum):

        def can_place(cur_sum):
            a0 = max(cur_sum - index, 0)
            an = max(cur_sum - (n - index - 1), 0)
            s1 = (a0 + cur_sum) * (cur_sum - a0 + 1) // 2
            s2 = (cur_sum - 1 + an) * (cur_sum - an) // 2
            return s1 + s2 <= maxSum

        # below row is filled by 1
        maxSum -= n
        hi = maxSum
        lo = 0
        while lo < hi:
            # max at index
            mid = (lo + hi + 1) // 2
            if can_place(mid):
                lo = mid
            else:
                hi = mid - 1
        # + 1 to count the below row.
        return lo + 1

sol = Solution()
print(sol.maxValue(n = 6, index = 1,  maxSum = 10))#3
print(sol.maxValue(n = 4, index = 2,  maxSum = 6))#2