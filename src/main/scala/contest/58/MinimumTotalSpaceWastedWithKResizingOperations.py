from math import inf


class Solution:
    def minSpaceWastedKResizing(self, nums, k: int) -> int:
        n = len(nums)
        dp = [[-1] * (k+1) for _ in range(n)]

        def find_min_wasted(dp, i, k):
            if i == len(nums):
                return 0
            if k < 0:
                return inf
            if dp[i][k] >= 0:
                return dp[i][k]
            sum_of_num = 0
            max_so_far = nums[i]
            ans = inf
            for j in range(i, len(nums)):
                max_so_far = max(max_so_far, nums[j])
                sum_of_num += nums[j]
                #try to resize the at max_so_far
                wasted = (j - i + 1) * max_so_far - sum_of_num
                ans = min(ans, find_min_wasted(dp, j + 1, k - 1) + wasted)
            dp[i][k] = ans
            return ans

        return find_min_wasted(dp, 0, k)


sol = Solution()
print(sol.minSpaceWastedKResizing([10,20,15,30,20], 2))  # 15
print(sol.minSpaceWastedKResizing([1, 48, 18], 1))  # 30
