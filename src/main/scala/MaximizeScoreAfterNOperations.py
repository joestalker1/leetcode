class Solution:
    def maxScore(self, nums: List[int]) -> int:
        if not nums or len(nums) == 1:
            return 0

        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)

        dp = [[-1] * (2 ** (len(nums) + 1)) for _ in range(len(nums) + 1)]

        def max_gcd(dp, t, mask):
            if t > len(nums) // 2:
                return 0
            if dp[t][mask] != -1:
                return dp[t][mask]
            for k in range(len(nums)):
                for l in range(k + 1, len(nums)):
                    new_mask = (1 << k) + (1 << l)
                    # check if items are not used already
                    if new_mask & mask:
                        continue
                    dp[t][mask] = max(dp[t][mask], t * gcd(nums[k], nums[l]) + max_gcd(dp, t + 1, mask + new_mask))
            return dp[t][mask]

        return max_gcd(dp, 1, 0)
