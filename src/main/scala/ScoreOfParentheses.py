class Solution(object):
    def scoreOfParentheses(self, S):
        score = 0
        core = 0
        for i in range(len(S)):
            if S[i] == '(':
                core += 1
            else:
                core -= 1
                # case ()
                if S[i-1] == '(':
                    score += 1 << core
        return score