class Solution:
    def repeatedSubstringPattern(self, s):
        res = False
        to = len(s) // 2
        for l in range(1, to + 1):
            sub = s[0:l]
            j = l
            res = True
            while j < len(s) - l:
                k = j
                for ch in sub:
                    if ch != s[k]:
                        j = len(s)
                        res = False
                        break
                    k += 1
                j += l

        return res


sol = Solution()
print(sol.repeatedSubstringPattern("ababa"))
