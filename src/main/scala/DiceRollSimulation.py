class Solution(object):
    def dieSimulator(self, n, rollMax):
        if n == 0 or not rollMax:
            return 0

        dp = [[0 for _ in range(6)] for _ in range(n)]
        for i in range(n):
            for j in range(6):
                for x in range(1, rollMax[j] + 1):
                    if i - x >= 0:
                        for v in range(6):
                            if v != j:
                                dp[i][j] = dp[i][j] + dp[i - x][v]
                    else:
                        dp[i][j] += 1
                        break

        return sum(dp[n-1])

sol = Solution()
#print(sol.dieSimulator(5000, [13,3,12,14,11,11]))
#print(sol.dieSimulator(10, [2,7,1,2,6,5]))
print(sol.dieSimulator(n = 3, rollMax = [1,1,1,2,2,3]))#181
#print(sol.dieSimulator(3, [1,3,3]))
#print(sol.dieSimulator(n = 2, rollMax = [1,1,1,1,1,1]))#30
print(sol.dieSimulator(n = 3, rollMax = [1,1,2,2,2,3]))#34

# 2:2->5
# 2:3->5
# 2:4->6
# 2:5->6
# 2:6->6
# 1:1->28
# 2:1->5
# 2:3->5
# 2:4->6
# 2:5->6
# 2:6->6
# 1:2->28
# 2:1->5
# 2:2->5
# 2:4->6
# 2:5->6
# 2:6->6
# 1:3->28
# 2:1->5
# 2:2->5
# 2:3->5
# 2:4->5
# 2:5->6
# 2:6->6
# 1:4->32
# 2:1->5
# 2:2->5
# 2:3->5
# 2:4->6
# 2:5->5
# 2:6->6
# 1:5->32
# 2:1->5
# 2:2->5
# 2:3->5
# 2:4->6
# 2:5->6
# 2:6->6
# 1:6->33
# 0:-1->181