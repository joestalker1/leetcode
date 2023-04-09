class Solution:
    def maximizeWin(self, prizePositions, k: int) -> int:
        left = 0
        right = 0
        dp = [0] * len(prizePositions)
        max_prize_num = 0
        while right < len(prizePositions):
            while prizePositions[right] - prizePositions[left] > k:
                left += 1
            cur_prize_num = right - left + 1
            #dp[left-1] is prize number in left segment
            max_prize_num = max(max_prize_num, cur_prize_num + (dp[left-1] if left > 0 else 0))
            # dp[righ - 1] is prize number in curent segment < k
            dp[right] = max(dp[right-1] if right > 0 else 0, cur_prize_num)
            right += 1
        return max_prize_num
    