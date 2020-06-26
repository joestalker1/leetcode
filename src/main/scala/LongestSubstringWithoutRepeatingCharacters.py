class Solution:
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0
        max_len = 0
        i1 = 0
        i2 = 0
        m = {}
        while i2 < len(s):
            if s[i2] in m:
                i1 = max(m[s[i2]], i1)
            max_len = max(max_len, i2 - i1)
            m[s[i2]] = i2
            i2 += 1
        return max_len

