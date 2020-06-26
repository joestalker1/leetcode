class Solution:
    def trap(self, height):
        if not height:
            return 0
        cap = 0
        st = []
        for i in range(len(height)):
            while st and height[st[-1]] < height[i]:
                top = st.pop()
                if not st:
                    break
                dist = i - st[-1] - 1  # dist from last - top of stack
                h = min(height[i], height[st[-1]]) - height[
                    top]  # heigh of min current(right bar) or top of stack(left bar) - popped bar(middle part)
                cap += h * dist
            st.append(i)
        return cap


sol = Solution()
print(sol.trap([2, 0, 2]))  # 2
print(sol.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
