class Solution:
    def numSubmat(self, mat):
        n = len(mat)
        m = len(mat[0])
        res = 0
        #count one right of [i,j]
        for i in range(n):
            c = 0
            counts = [0] * m
            for j in range(m - 1, -1, -1):
                if mat[i][j] == 1:
                    c+=1
                else:
                    c = 0
                counts[j] = c

            for j in range(m):
                #for every [i,j] is topleft point
                t = float('inf')
                #count one number for every row from i to n
                for k in range(i, n):
                    t = min(t, counts[j])
                    res += t
        return res


                    

