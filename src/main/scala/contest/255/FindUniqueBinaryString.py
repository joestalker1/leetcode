class Solution:
    def minimizeTheDifference(self, mat, target: int) -> int:
        ans = 0
        for i in range(len(mat)):
            max_diff = -1
            k = 0
            for j in range(len(mat[0])):
                if abs(mat[i][j] - target) > max_diff:
                    k = j
                    max_diff = abs(mat[i][j] - target)
            ans += mat[i][k]
        return abs(ans - target)


sol = Solution()
print(sol.minimizeTheDifference([[1,2,3],[4,5,6],[7,8,9]],13))