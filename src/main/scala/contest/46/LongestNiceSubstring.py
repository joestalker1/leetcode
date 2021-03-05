class Solution:
    def longestNiceSubstring(self, s):
        if not s or len(s) == 1:
            return ''
        niceChars = {ch: False for ch in s if ch.islower()}
        for ch in s:
            if ch.isupper():
                niceChars[ch.lower()] = True
        #all chars with zero is candidates for nice substring
        res = []
        for i in range(len(s) - 1):
            niceStr = []
            for j in range(i, len(s)):
                niceStr.append(s[j])
                #check if niceStr is nice
                lc = set(niceStr)
                nice = True
                for ch in niceStr:
                    if ch.islower() and ch.upper() not in lc or ch.isupper and ch.lower() not in lc:
                        nice = False
                        break
                if nice and len(niceStr) > len(res):
                    res = list(niceStr)
        return ''.join(res)


sol = Solution()
print(sol.longestNiceSubstring("dDzeE"))
print(sol.longestNiceSubstring("YazaAay"))

