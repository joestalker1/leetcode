class Solution:
    def strStr(self, haystack, needle):
        if len(haystack) < len(needle):
            return -1
        i = 0
        len1 = len(haystack)
        len2 = len(needle)
        while i <= len1 - len2:
            i1 = i
            j = 0
            while j < len2 and haystack[i1] == needle[j]:
                i1 += 1
                j += 1
            if j == len2:
                return i
            i += 1
        return -1

sol = Solution()
print(sol.strStr("", ""))
print(sol.strStr("hello", "ll"))