class Solution:
    def isAnagram(self, s, t):
        if len(s) == 0 and len(t) == 0:
            return True
        map1 = {}
        for i in range(len(s)):
            if s[i] in map1:
                c = map1[s[i]]
                map1[s[i]] = c + 1
            else:
                map1[s[i]] = 1

        for i in range(len(t)):
            if t[i] not in map1:
                return False
            c = map1[t[i]] - 1
            if c == 0:
                del t[t[i]]
            else:
                map1[t[i]] = c
        if len(map1) > 0:
            return False
        else:
            return True

s = input()
t = input()
sol = Solution()
print(sol.isAnagram(s, t))