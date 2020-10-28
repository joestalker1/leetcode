class Solution:
    def validateStackSequences(self, pushed, popped):
        st = []
        j = 0
        for x in pushed:
            pushed.append(x)
            while st and st[-1] == popped[j]:
                st.pop()
                j += 1
        return j == len(popped)



sol = Solution()
print(sol.validateStackSequences([2,1,0], [1,2,0]))#true


