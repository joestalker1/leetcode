class Solution(object):
    def findDiagonalOrder(self, matrix):
        if not matrix or not matrix[0]:
            return []
        res = []
        r = 0
        c = 0
        d1 = -1
        d2 = 1
        count = len(matrix) * len(matrix[0])
        while count > 0:
            res.append(matrix[r][c])
            if r + d1 < 0 or r + d1 == len(matrix):
                if c + 1 == len(matrix[0]):
                    r += 1
                else:
                    c += 1
                d1 = -d1
                d2 = -d2
            elif c + d2 < 0 or c + d2 == len(matrix[0]):
                if r + 1 == len(matrix):
                    c += 1
                else:
                    r += 1
                d1 = -d1
                d2 = -d2
            else:
                r += d1
                c += d2
            count -= 1
        return res

sol = Solution()
print(sol.findDiagonalOrder([
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
])) #[1,2,4,7,5,3,6,8,9]




