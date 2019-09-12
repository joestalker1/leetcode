class Solution:
      def canMakePaliQueries(self, s, queries):
        if not s or not queries:
            return []
        dp = [[0] * 26]
        for i in range(1, len(s) + 1):
            new_dp = dp[i-1][:]
            new_dp[ord(s[i - 1]) - ord('a')] += 1
            dp.append(new_dp)
        answer = []
        for start,end,may_change in queries:
            R = dp[end + 1]
            L =  dp[start]
            odds = sum((R[i] - L[i]) & 1 for i in range(26))
            if odds // 2 <= may_change:
                answer.append(True)
            else:
                answer.append(False)
        return answer


sol = Solution()
print(sol.canMakePaliQueries("abcda", [[1,2,0]]))
print(sol.canMakePaliQueries("hunu", [[0,3,1]]))#true
print(sol.canMakePaliQueries("hunu", [[1,1,1],[2,3,0],[3,3,1],[0,3,2],[1,3,3],[2,3,1],[3,3,1],[0,3,0],[1,1,1],[2,3,0],[3,3,1],[0,3,1],[1,1,1]]))
print(sol.canMakePaliQueries(s = "abcda", queries = [[0,3,2]]))#true
print(sol.canMakePaliQueries(s = "abcda", queries = [[3,3,0],[1,2,0],[0,3,1],[0,3,2],[0,4,1]]))








