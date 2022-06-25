class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not haystack or not needle:
            return -1

        def build_zarray(s):
            n = len(s)
            z = [0] * n
            l = 0
            r = 0
            k = 0
            for i in range(1, n):
                if i > r:
                    l = r = i
                    while r < n and s[r - l] == s[r]:
                        r += 1
                    z[i] = r - l
                    r -= 1
                else:
                    k = i - l
                    if z[k] < r - i + 1:
                        z[i] = z[k]
                    else:
                        l = i
                        while r < n and s[r - l] == s[r]:
                            r += 1
                        z[i] = r - l
                        r -= 1
            return z

        s = needle + '$' + haystack
        z = build_zarray(s)
        for i in range(len(s)):
            if z[i] == len(needle):
                return i - len(needle) - 1
        return -1