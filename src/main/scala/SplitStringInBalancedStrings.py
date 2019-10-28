class Solution(object):
    def balancedStringSplit(self, s):
        if not s:
            return 0

        def is_balanced_string(pos, len_string):
            i = pos
            ch = s[i]
            while i < (pos + len_string) and s[i] == ch:
                i += 1
            j = i
            ch = s[j]
            while j < (pos + len_string) and s[j] == ch:
                j += 1
            return (i - pos) == (j - i)

        def split(pos):
            if pos == len(s):
                return 0
            max_len = 0
            for l in range(2, len(s) + 1):
                for i in range(pos, len(s) - l + 1):
                    if not is_balanced_string(i, l):
                        break
                    len_s = 1 + split(pos + l)
                    max_len = max(max_len, len_s)
            return max_len

        return split(0)

sol = Solution()
print(sol.balancedStringSplit("RRLRRLRLLLRL"))#2
print(sol.balancedStringSplit("LLLLRRRR"))
print(sol.balancedStringSplit("RLLLLRRRLR"))
print(sol.balancedStringSplit("RLRRLLRLRL"))







