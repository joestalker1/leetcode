class Solution:
    def largestRectangleArea(self, heights):
        max_area = 0
        # consider heights[L] ... heights[j] ... heights[R]
        #where where we check if heights[i] is R for stack top element
        #put L is -1
        st = [-1]
        #last R is len(heights)
        for i in range(len(heights)):
            #push items in increasing order until we get item is less stack top and it will be R for stack top
            R = i
            while st[-1] != - 1 and heights[st[-1]] >= heights[i]:
                t = st.pop()
                L = st[-1]
                # for t: L is stack top and R is current heights[i]
                max_area = max(max_area, heights[t] * (R - L - 1))
            st.append(i)
        # R is len(heights)
        R = len(heights)
        while st[-1] != -1:
            t = st.pop()
            L = st[-1]
            # for heights[t]: L is stack top and R is len(heights)
            max_area = max(max_area, heights[t] * (R - L - 1))
        return max_area




sol = Solution()
print(sol.largestRectangleArea([2,1,2]))#3
print(sol.largestRectangleArea([0, 0, 0, 0, 0, 0, 0, 0, 2147483647]))
print(sol.largestRectangleArea([2, 1, 5, 6, 2, 3]))#10
