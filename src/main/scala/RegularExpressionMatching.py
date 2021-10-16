class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s
        first_match = s and (s[0] == p[0] or p[0] == '.')
        if len(p) >= 2 and p[1] == '*':
            return self.isMatch(s,p[2:]) or first_match and self.isMatch(s[1:], p)
        else:
            return first_match and self.isMatch(s[1:],p[1:])


sol = Solution()
print(sol.isMatch("aa","a*"))#true
print(sol.isMatch("aaa", "a*a"))#true
print(sol.isMatch("ab",".*"))#true
print(sol.isMatch("a","a*c"))#false
print(sol.isMatch("a", "ab*"))#true
print(sol.isMatch("aa", "a*"))#true