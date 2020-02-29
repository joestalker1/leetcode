class Solution:
    def minRemoveToMakeValid(self, s):
        if not s:
            return []
        open_seen = 0
        balance = 0
        chars = []
        # remove ')'
        for c in s:
            if c == '(':
                open_seen += 1
                balance += 1
            elif c == ')':
                if balance == 0:
                    continue
                balance -= 1
            chars.append(c)
        keep_open = open_seen - balance
        res = []
        # remove '('
        for c in chars:
            if c == '(':
                if keep_open == 0:
                    continue
                keep_open -= 1
            res.append(c)
        return ''.join(res)

sol = Solution()
print(sol.minRemoveToMakeValid("))(("))
print(sol.minRemoveToMakeValid("lee(t(c)o)de)"))

