class Solution:
    def findRotation(self, mat, target) -> bool:
        n = len(mat)
        rotated = [[0] * n for _ in range(n)]

        def is_equal(mat1, mat2):
            for i in range(n):
                for j in range(n):
                    if mat1[i][j] != mat2[i][j]:
                        return False
            return True

        for _ in range(3):
            for i in range(n):
                for j in range(n):
                    rotated[j][n - 1 - i] = mat[i][j]
            # compare rotated and target
            if is_equal(rotated, target):
                return True
            mat,rotated = rotated,mat
        return False


sol = Solution()
print(sol.findRotation([[1,1],[0,1]],[[1,1],[1,0]]))#true
print(sol.findRotation([[0, 0, 0], [0, 1, 0], [1, 1, 1]], [[1, 1, 1], [0, 1, 0], [0, 0, 0]]))#true
