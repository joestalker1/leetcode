class Solution:
    def isIsomorphic(self, s, t):
        if len(s) == 0:
            return True
        else:
            map1 = {}
            map2 = {}
            for i in range(len(s)):
                if s[i] in map1:
                    ti = map1[s[i]]
                    if ti != t[i]:
                        return False
                else:
                    if t[i] in map2:
                        si = map2[t[i]]
                        if si != s[i]:
                            return False
                    map1[s[i]] = t[i]
                    map2[t[i]] = s[i]

            return True


s = input()
t = input()
sol = Solution()
print(sol.isIsomorphic(s, t))