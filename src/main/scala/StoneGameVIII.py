class Solution:
    def stoneGameVIII(self, stones) -> int:
        if len(stones) < 2:
            return 0
        # calculate prefix sum
        # ) I merge the first 2 two I get 3 points and A becomes [3,3,4].#
        # b) You merge the first two you get 6 points and A becomes [6,4].
        # c) I merge the last two and get 10 points. Game stops.

        # The score difference you got in step b) is 6 - 10 = -4 where 6 is yourScore and 10 is myScore.

        # Now backtrack to step a), my total score is prefix[1] + myScore = 3 + 10 = 13, and the score difference I get is 13 - 6 = 7 which is the same as 3 - (-4) = 7.

        # Try running the algorithm with some examples and you will get it.
        pr = [0] * len(stones)
        pr[0] = stones[0]
        for i in range(1, len(stones)):
            pr.append(pr[-1] + stones[i])

        # dp = [0] * len(stones)
        # dp[-1] = pr[-1]
        max_diff = pr[-2]
        for i in range(len(stones) - 1):
            scoreA = pr[i]
            for j in range(i + 1, len(stones) - 1):
                max_diff = max(pr[j] - pr[i], max_diff)
        return max_diff