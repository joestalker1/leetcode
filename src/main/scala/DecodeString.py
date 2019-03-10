class Decoded:
    def __init__(self):
        self.pos = 0
        self.res = ''


class Solution:
    def is_digit(self, ch):
        return '0' <= ch <= '9'

    def is_char(self, ch):
        return 'a' <= ch <= 'z' or 'A' <= ch <= 'Z'

    def str(self, s, decoded):
        if decoded.pos == len(s):
            return ""
        if self.is_char(s[decoded.pos]):
            j = decoded.pos
            while decoded.pos < len(s) and self.is_char(s[decoded.pos]):
                decoded.pos += 1
            decoded.res += s[j: decoded.pos]

    def rep_or_str(self, s, decoded):
        if decoded.pos == len(s):
            return ""
        if self.is_char(s[decoded.pos]):
            self.str(s, decoded)
            return
        j = decoded.pos
        while decoded.pos < len(s) and self.is_digit(s[decoded.pos]):
            decoded.pos += 1
        k = int(s[j: decoded.pos])
        decoded.pos += 1
        prev = decoded.pos
        for i in range(k):
            decoded.pos = prev
            while s[decoded.pos] != ']':
                self.str(s, decoded)
                if self.is_digit(s[decoded.pos]):
                    self.rep_or_str(s, decoded)
                elif self.is_char(s[decoded.pos]):
                    self.str(s, decoded)
            decoded.pos += 1

    def decodeString(self, s: str) -> str:
        if not str:
            return ""
        decoded = Decoded()
        while decoded.pos < len(s):
            self.rep_or_str(s, decoded)
        return decoded.res


sol = Solution()
print(sol.decodeString("3[a]2[b4[F]c]"))
print(sol.decodeString("2[abc]3[cd]ef"))
print(sol.decodeString("3[a2[c]]"))
print(sol.decodeString("3[a]2[bc]"))
