from math import ceil

class Solution:
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        n = len(s)
        sect = ceil(n / (2*numRows - 2.0))
        num_cols = sect * (numRows - 1)
        zigzag = [[0] * num_cols for _ in range(numRows)]
        r = 0
        c = 0
        i = 0
        while i < n:
            while i < n and r < numRows:
                zigzag[r][c] = s[i]
                i += 1
                r += 1
            r -= 2
            c += 1
            while i < n and r > 0 and c < num_cols:
                zigzag[r][c] = s[i]
                r -= 1
                c += 1
                i += 1
        res = []
        for i in range(len(zigzag)):
            for j in range(len(zigzag[0])):
                if zigzag[i][j] != 0:
                    res.append(zigzag[i][j])
        return ''.join(res)


sol = Solution()
print(sol.convert("PAYPALISHIRING", 4))

