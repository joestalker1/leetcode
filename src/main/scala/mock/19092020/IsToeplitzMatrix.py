class Solution:
    def isToeplitzMatrix(self, matrix):
        if not matrix or not matrix[0]:
            return False
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            r = i + 1
            c = 1
            while r < n and c < m:
                if matrix[r - 1][c - 1] != matrix[r][c]:
                    return False
                r += 1
                c += 1
        for j in range(1, m):
            c = j + 1
            r = 1
            while r < n and c < m:
                if matrix[r - 1][c - 1] != matrix[r][c]:
                    return False
                c += 1
                r += 1
        return True


sol = Solution()
arr = [[36, 59, 71, 15, 26, 82, 87], [56, 36, 59, 71, 15, 26, 82], [15, 0, 36, 59, 71, 15, 26]]
print(sol.isToeplitzMatrix(arr)) # false
