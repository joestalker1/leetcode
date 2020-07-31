class Solution:
    def licenseKeyFormatting(self, S: str, K: int):
        if not S:
            return S
        res = []
        for i in range(len(S) - 1, -1, K):
            i = max(0, i - K + 1)
            sub = S[i:i + K]
            res.append(sub.upper())
        R = res[0]
        for i in range(len(res)):
            R += '-{}'.format(res[i])
        return R
