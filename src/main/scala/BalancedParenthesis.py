class Solution:
    def balanceParent(self, n):

        def generate(open, close, res, buf):
            if close == n:
                res.append(buf)
                return
            if close < open:
                generate(open, close + 1, res, buf + '}')
            if open < n:
                generate(open + 1, close, res, buf + '{')

        res = []
        generate(0, 0, res, '')
        return res


sol = Solution()
print(sol.balanceParent(3))
