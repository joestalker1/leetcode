class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        res = [0] * n
        st = []
        # go from right to left
        # keep increasing order
        for i in range(n-1, -1, -1):
            while st and st[-1] < heights[i]:
                st.pop()
                res[i] +=1
            if st:
                #+1 for person is higher than current one
                res[i] += 1
            st.append(heights[i])
        return res 