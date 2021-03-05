class Solution:
    def maximalRectangle(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        n = len(matrix)
        m = len(matrix[0])
        heights = [0] * m
        max_rect = 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0
            #calculate the histogram area:
            # consider: heights[L] < heights[i] >= heights[R]
            # for leftmost items -1 performs as L, m does as R
            st = [-1]
            for j in range(m):
                #push itme in increasing order until we find the heights[R] < stack top.
                while st[-1] != -1 and heights[st[-1]] >= heights[j]:
                    # l is the item we calculate the area for.
                    l = st.pop()
                    #st[-1] is L, R is current j
                    max_rect = max(max_rect, heights[l] * (j - st[-1] - 1))
                st.append(j)
            #it's left to consider m as R for rest of itmes in stack
            while st[-1] != -1:
                l = st.pop()
                #L is stack[top-1]
                max_rect = max(max_rect, heights[l]*(m - st[-1] - 1))
        return max_rect

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
