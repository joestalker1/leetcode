class Solution(object):
    def longestArithSeqLength(self, A):
        if not A:
            return 0
        las = [1] * 20001
        for i in range(len(las)):
            las[i] = [1] * len(A)
        max_len = 0
        for i in range(len(A)):
            for j in range(i):
                d = A[i] - A[j]
                las[2001 + d][i] = max(las[2001 + d][i], las[2001 + d][j] + 1)
                max_len = max(max_len, las[2001 + d][i])
        return max_len

sol = Solution()
print(sol.longestArithSeqLength([20,1,15,3,10,5,8]))
print(sol.longestArithSeqLength([9,4,7,2,10]))
print(sol.longestArithSeqLength([3,6,9,12]))


