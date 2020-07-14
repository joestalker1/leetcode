class Solution:
    def largestRectangleArea(self, heights):
        max_area = 0
        st = [-1]
        for i in range(len(heights)):
            while st[-1] != - 1 and heights[st[-1]] >= heights[i]:
                max_area = max(max_area, heights[st.pop()] * (i - st[-1] - 1))
            st.append(i)

        while st[-1] != -1:
            max_area = max(max_area, heights[st.pop()] * (len(heights) - st[-1] - 1))
        return max_area


sol = Solution()
#print(sol.largestRectangleArea([0, 0, 0, 0, 0, 0, 0, 0, 2147483647]))
print(sol.largestRectangleArea([5, 6, 2, 3]))
