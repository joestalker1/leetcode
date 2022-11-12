class Solution:
    def maximumRows(self, mat, cols: int) -> int:
        # assert self._maximumRows([[0,1],[1,0]],2) == 2,'test1'
        return self._maximumRows(mat, cols)

    def _maximumRows(self, mat, cols: int) -> int:
        if len(mat[0]) == 1:
            return len(mat)
        n = len(mat)
        m = len(mat[0])
        max_cnt = 0
        for i in range(n):
            added_cols = 0
            selected_cols = 0
            for j in range(m):
                if mat[i][j] == 1:
                    selected_cols |= (1 << j)
                    added_cols += 1
            cnt = 0
            for j in range(n):
                cur_selected_cols = selected_cols
                new_added_cols = added_cols
                for k in range(m):
                    if new_added_cols > cols:
                        break
                    if mat[j][k] == 1 and ((cur_selected_cols >> k) & 1) == 0:
                        cur_selected_cols |= (1 << k)
                        new_added_cols += 1
                if new_added_cols <= cols:
                    cnt += 1
                    selected_cols = cur_selected_cols
                    added_cols = new_added_cols
            max_cnt = max(max_cnt, cnt)
        return max_cnt


sol = Solution()
print(sol.maximumRows([[0,1],[1,0]],2))#2
print(sol.maximumRows([[0,0,0],[1,0,1],[0,1,1],[0,0,1]],2))#3