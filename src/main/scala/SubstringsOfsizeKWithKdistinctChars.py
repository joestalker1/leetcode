class Solution:
    def substringLengthK(self, s, k):
        if not s or k == 0:
            return []

        words = set()
        j = 0
        chars = [0] * 27
        char_num = 0

        def code(ch):
            return ord(ch) - ord('a')

        for i in range(len(s)):
            chars[code(s[i])] += 1
            if chars[code(s[i])] == 1:
                char_num += 1
            if i - j + 1 == k:
                if char_num == k:
                    words.add(s[j:i + 1])
                chars[code(s[j])] -= 1
                if chars[code(s[j])] == 0:
                    char_num -= 1
                j += 1

        return list(words)


sol = Solution()
print(sol.substringLengthK(s="awaglknagawunagwkwagl", k=4))
print(sol.substringLengthK(s="abcabc", k=3))
