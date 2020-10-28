class Solution:
    def numSubmat(self, mat):
        if not mat or not mat[0]:
            return 0

        n = len(mat)
        m = len(mat[0])
        dp = {}

        count = 0
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1:
                    dp[(i,j,1,1)] = 1
                    count += 1
        for l1 in range(1, n + 1):
            for l2 in range(1, m + 1):
                for r in range(n - l1 + 1):
                    for c in range(m - l2 + 1):
                        if l1 > 1 and l2 > 1:
                            k1 = (r, c, l1 - 1, l2)
                            k2 = (r, c, l1, l2 - 1)
                            if k1 in dp and k2 in dp and mat[r + l1 - 1][c + l2 - 1] == 1:
                                dp[(r, c, l1, l2)] = True
                                count += 1
                        elif l1 == 1 and l2 > 1:#horizontal
                            k2 = (r, c, 1, l2 - 1)
                            if k2 in dp and mat[r][c + l2 - 1] == 1:
                                dp[(r, c, l1, l2)] = True
                                count += 1
                        elif l1 > 1 and l2 == 1: #vertical
                            k1 = (r, c, l1 - 1, 1)
                            if k1 in dp and mat[r + l1 - 1][c] == 1:
                                dp[(r, c, l1, l2)] = True
                                count += 1

        return count


sol = Solution()
print(sol.numSubmat([[1,1,1,1,1,1]]))

print(sol.numSubmat([[0, 1, 1, 0],
                     [0, 1, 1, 1],
                     [1, 1, 1, 0]])) #24
print(sol.numSubmat([[1, 0, 1],
                     [1, 1, 0],
                     [1, 1, 0]]))
