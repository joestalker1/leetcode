class Solution:
    def firstUniqChar(self, s):
        if not s:
            return None
        m = {}
        for i in range(len(s)):
            if s[i] not in m:
                m[s[i]] = i
            else:
                m[s[i]] = -1
        i = float("inf")
        for _,j in m.items():
            if -1 < j < i:
                i = j
        return i

sol = Solution()
print(sol.firstUniqChar("loveleetcode"))
print(sol.firstUniqChar("leetcode"))
