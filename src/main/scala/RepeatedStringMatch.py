class Solution:
    def repeatedStringMatch(self, A, B):
        sa = A
        c = 1
        while (len(sa)-len(B)) <= len(B):
            if sa.find(B) != -1:
                return c
            sa += A
            c += 1
        if sa.find(B) != -1:
            return c
        return -1



sol = Solution()
print(sol.repeatedStringMatch("aabaa", "aaab")) # 2
print(sol.repeatedStringMatch( "abcd", "cdabcdab"))
print(sol.repeatedStringMatch("abcd", "abcdb"))
