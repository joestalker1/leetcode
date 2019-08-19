class Solution:
    def generateMatrix(self, n):
        if n == 0:
            return [[]]
        if n == 1:
            return [[n]]
        new_size = n ** 2
        mat = [0] * n
        for i in range(len(mat)):
            mat[i] = [0] * n
        num = 1
        # to the left
        r1 = 0
        c1 = 0
        while num <= new_size:
            r2 = r1 + n - 1
            c2 = c1 + n - 1
            if num == new_size:
                mat[r1][c1] = num
                num += 1
                break
            #to the left
            for j in range(c1, c2 + 1):
                mat[r1][j] = num
                num += 1
            #to the bottom
            for i in range(r1 + 1, r2 + 1):
                mat[i][c2] = num
                num += 1
            #to the left
            a = num + n - 2
            for j in range(c1, c2):
                mat[r2][j] = a
                a -= 1
            num = mat[r2][c1] + 1
            #to the top
            for i in range(r2 - 1, r1, -1):
                mat[i][c1] = num
                num += 1
            r1 += 1
            c1 += 1
            n -= 2
        return mat


sol = Solution()
print(sol.generateMatrix(3))
print(sol.generateMatrix(4))