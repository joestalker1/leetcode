class Solution:
    def isPrefixString(self, s: str, words) -> bool:
        if not s or not words:
            return False
        start = 0
        for i in range(len(words)):
            if start == len(s):
                return True
            if len(s) - start < len(words[i]):
                return False
            if s[start:start + len(words[i])] == words[i]:
                start += len(words[i])
            else:
                break
        return start == len(s)


sol = Solution()
print(sol.isPrefixString('z', ['z']))