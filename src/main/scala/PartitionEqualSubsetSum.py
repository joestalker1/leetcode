class Solution:
    def canPartition(self, nums) -> bool:
        if len(nums) < 2:
            return False
        sum_of_arr = sum(nums)
        if sum_of_arr % 2 != 0:
            return False

        need_sum = sum_of_arr // 2
        dp = [0] * (sum_of_arr + 1)
        dp[nums[0]] = 1

        for i in range(1, len(nums)):
            new_dp = [0] * (sum_of_arr + 1)
            for cur_sum in range(need_sum + 1):
                # 2 cases: dp[i-1][cur_sum] if it has sum without nums[i] or with nums[i]
                if ((cur_sum - nums[i]) > 0 and dp[cur_sum - nums[i]] == 1) or dp[cur_sum] == 1:
                    if need_sum == cur_sum:
                        return True
                    new_dp[cur_sum] = 1
            dp = new_dp
        return False