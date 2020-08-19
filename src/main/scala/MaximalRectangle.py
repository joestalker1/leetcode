class Solution:
    def find_max_hist(self, hist):
        st = [-1] # oto
        max_area = 0
        for i in range(len(hist)):
            # pop if stack pop is greater then current height
            # push to the if current height < stack top
            while st[-1] != -1 and hist[st[-1]] >= hist[i]:
                j = st.pop()
                #calculate square left_mort, current histogram
                max_area = max(max_area, hist[j] * (i - st[-1] - 1))
            st.append(i)
        #if stack is not empty, let's pop this heights using len(hist) as left boundary
        while st[-1] != -1:
            max_area = max(max_area, hist[st.pop()] * (len(hist) - st[-1] - 1))

        return max_area

    def maximalRectangle(self, matrix):
        if not matrix:
            return 0
        n = len(matrix)
        m = len(matrix[0])
        dp = [0] * m
        max_area = 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == '1':
                    dp[j] = dp[j] + 1
                else:
                    dp[j] = 0
            max_area = max(max_area, self.find_max_hist(dp))
        return max_area


sol = Solution()
# print(sol.maximalRectangle([
#     ["1", "1"],
#     ["1", "1"],
#     ["1", "1"],
#     ["1", "1"]
# ]))
print(sol.maximalRectangle([
    ["1", "0", "1", "0", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "0", "1", "0"]
]))
