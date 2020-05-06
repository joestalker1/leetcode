class Solution:
    def generateParenthesis(self, n):
        if not n:
            return []
        res = []

        def paren(open, close, current, res):
            if len(current) == 2*n:
                res.append(current)
                return
            if open < n:
                paren(open+1,close,current+'(', res)
            if open > close:
                paren(open, close+1,current + ')', res)
        paren(0,0, '', res)
        return res


sol = Solution()
print(sol.generateParenthesis(5))