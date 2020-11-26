class Solution:
    def reorderSpaces(self, text):
        if not text:
            return text
        words = [w for w in text.split(' ') if w]
        total = len(text) - sum([len(w) for w in words])
        if total == 0:
            return text
        n = (len(words) - 1) if len(words) > 1 else 1
        sp = total // n
        res = []
        for i in range(len(words)):
            res.append(words[i])
            if i < len(words) - 1:
                res.append(' ' * sp)
                total -= sp
        if total > 0:
            res.append(' ' * total)
        return ''.join(res)


sol = Solution()
print(sol.reorderSpaces("a b   c d"))





