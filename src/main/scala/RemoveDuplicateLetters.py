from collections import Counter

class Solution:
    def removeDuplicateLetters(self, s):
        if not s:
            return s
        cnt = Counter(s)
        used = set()
        stack = []
        for i in range(len(s)):
            cnt[s[i]] -= 1
            if s[i] in used:
                continue
            while stack and s[i] < stack[-1] and cnt[stack[-1]] > 0:
                used.discard(stack[-1]) # to allow to add at second time
                stack.pop()
            stack.append(s[i])
            used.add(s[i])
        return ''.join(stack)



sol = Solution()
print(sol.removeDuplicateLetters("bbcaac"))
print(sol.removeDuplicateLetters("cbacdcbc"))#acdb"
print(sol.removeDuplicateLetters("bcabc"))#abc
print(sol.removeDuplicateLetters("abacb"))#"abc"



