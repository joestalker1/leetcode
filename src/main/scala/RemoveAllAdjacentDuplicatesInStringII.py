class Solution:
    def removeDuplicates(self, S: str):
        res = []
        for i in range(len(S)):
            res.append(S[i])
            while len(res) > 1 and res[-1] == res[-2]:
                res.pop()
                res.pop()
        return ''.join(res)