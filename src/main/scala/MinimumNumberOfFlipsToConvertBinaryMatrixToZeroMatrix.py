class Solution:
    def minFlips(self, mat):

        def mat_to_num(mat):
            a = 0
            for r in range(len(mat)):
                for c in range(len(mat[0])):
                    if mat[r][c] == 1:
                        a = a | (1 << (r * len(mat[0]) + c))
            return a

        def get_val(a, r, c):
            b = 1 << (r * len(mat[0]) + c)
            return 1 if (a & b) > 0 else 0

        def put_val(a,r,c, v):
            if v == 1:
                b = 1 << (r * len(mat[0]) + c)
                a = a | b
            else:
                b = 1 << (r * len(mat[0]) + c)
                b = ~ b
                a = a & b
            return a

        def num_to_mat(m):
            new_mat = [[0] * len(mat[0]) for _ in range(len(mat))]
            for r in range(len(mat)):
                for c in range(len(mat[0])):
                    new_mat[r][c] = get_val(m, r,c)
            return new_mat

        def generate(m):
            res = []
            for r in range(len(mat)):
                for c in range(len(mat[0])):
                    m1 = m
                    res.append(invert(m1, r, c))
            return res

        def invert(m, r ,c):
            if get_val(m, r, c) == 1:
                m = put_val(m, r, c, 0)
            else:
                m = put_val(m, r, c, 1)
            for r2, c2 in [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]:
                if 0 <= r2 < len(mat) and 0 <= c2 < len(mat[0]):
                    if get_val(m, r2, c2) == 1:
                        m = put_val(m, r2, c2, 0)
                    else:
                        m = put_val(m, r2, c2, 1)
            return m

        m = mat_to_num(mat)
        q = [[0, m]]
        seen = {m}
        while q:
            t,m = q.pop(0)
            if m == 0:
                return t
            for nei in generate(m):
                if nei not in seen:
                    q.append([t + 1, nei])
                    seen.add(nei)
        return -1


sol = Solution()
print(sol.minFlips([[0]]))
print(sol.minFlips([[1,1,1],[1,0,1],[0,0,0]]))
print(sol.minFlips([[0,0],[0,1]]))



