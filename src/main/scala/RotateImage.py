class Solution:
    def shift(self, matrix,r1,c1,r2,c2, shift_count):
        if r1 == r2 and c1 == c2:
            return
        #c1 to c2
        for _ in range(shift_count):
            a = matrix[r1][c1]
            for i in range(c1+1, c2+1):
                t = matrix[r1][i]
                matrix[r1][i] = a
                a = t
            #r1 to r2
            for i in range(r1 + 1, r2 + 1):
                t = matrix[i][c2]
                matrix[i][c2] = a
                a = t
             #c2 to c1
            for i in range(c2-1, c1-1, -1):
                t = matrix[r2][i]
                matrix[r2][i] = a
                a = t
            #r2 to r1
            for i in range(r2-1, r1-1, -1):
                t = matrix[i][c1]
                matrix[i][c1] = a
                a = t

    def rotate(self, matrix):
        if not matrix:
            return matrix
        r1 = 0
        c1 = 0
        r2 = len(matrix)-1
        c2 = len(matrix[0]) - 1
        shift_count = len(matrix)-1
        while shift_count:
            self.shift(matrix,r1,c1,r2,c2, shift_count)
            r1 += 1
            c1 += 1
            r2 -= 1
            c2 -= 1
            shift_count -= 2
        return matrix

sol = Solution()
print(sol.rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))

print(sol.rotate([
  [1,2,3],
  [4,5,6],
  [7,8,9]
]))

