class Solution:
    def reverseWords(self, s):
        stack = []
        res = ''
        for i in range(len(s)):
            if s[i] != ' ':
                stack.append(s[i])
            elif s[i] == ' ':
               while len(stack) > 0:
                   stack.pp