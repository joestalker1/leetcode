class Solution:
    def __init__(self):
        self.pos = 0

    def is_digit(self, ch):
        return '0' <= ch <= '9'

    def is_char(self, ch):
        return 'a' <= ch <= 'z' or 'A' <= ch <= 'Z'

    def word(self, s):
        buf = []
        while self.pos < len(s) and self.is_char(s[self.pos]):
            buf.append(s[self.pos])
            self.pos += 1
        return ''.join(buf)

    def rep(self, s):
        num = []
        while self.is_digit(s[self.pos]) and self.pos < len(s):
            num.append(s[self.pos])
            self.pos += 1
        num = int(''.join(num))
        self.pos += 1  # for [
        # processing rest chars inside []
        next_term = self.rep_or_word(s)
        if self.pos < len(s) and s[self.pos] == ']':
            self.pos += 1

        return next_term * num

    def rep_or_word(self, s):
        res = ''
        while self.pos < len(s) and s[self.pos] != ']':
            if self.is_char(s[self.pos]):
                res += self.word(s)
            else:
                res += self.rep(s)
        return res

    def decodeString(self, s):
        if not str:
            return ""
        self.pos = 0
        return self.rep_or_word(s)


sol = Solution()
print(sol.decodeString("3[a]2[b4[F]c]"))#
#print(sol.decodeString("3[a]2[b4[F]c]"))
#print(sol.decodeString("2[abc]3[cd]ef"))#"abcabccdcdcdef"
#print(sol.decodeString("3[a2[c]]"))
print(sol.decodeString("3[a]2[bc]"))
