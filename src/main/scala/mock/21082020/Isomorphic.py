class Solution:
    def isIsomorphic(self, s: str, t: str):
        if not s and not t:
            return True
        if len(s) != len(t):
            return False

        m = {}
        for i in range(len(s)):
            ch1 = s[i]
            ch2 = t[i]
            if ch1 in m:
                if m[ch1] != ch2:
                    return False
            else:
                m[ch1] = ch2
        return True


sol = Solution()
print(sol.isIsomorphic("paper","title"))
print(sol.isIsomorphic(s = "foo", t = "bar"))
print(sol.isIsomorphic(s = "egg", t = "add"))