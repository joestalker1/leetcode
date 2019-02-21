class Solution(object):
    def copy_from_stack(self, word, ns):
        if len(ns) and len(word):
            ns.append(' ')
        while len(word):
            ns.append(word.pop())

    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s or len(s) == 0:
            return s
        s = list(s[::-1])
        word = []
        ns = []
        for i in range(len(s)):
            if s[i] != ' ':
                word.append(s[i])
            elif s[i] == ' ':
                self.copy_from_stack(word, ns)
        self.copy_from_stack(word, ns)
        return ''.join(ns).strip()


sol = Solution()
print(sol.reverseWords("   a   b "))
print(sol.reverseWords("the sky is blue"))