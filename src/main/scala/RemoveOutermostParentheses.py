class Solution:
    def removeOuterParentheses(self, S):
        if not S:
            return S
        parn = 0
        outers = []
        left = None
        for i in range(len(S)):
            if S[i] == ')':
                if parn == 1:
                    outers.append([left, i])
                parn -= 1
            else:
                if parn == 0:
                    left = i
                parn += 1
        res = []
        for a,b in outers:
            res.append(S[a:b+1])
        return ''.join(res)

