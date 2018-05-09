class Solution:
    def copy(self, s, start, end):
        l = end - start
        j = start
        while l >= 0:
            a = s[j]
            s[j] = s[j + l]
            s[j + l] = a
            l -= 2
            j += 1

    def reverseWords(self, s):
        start = -1
        end = -1
        s = list(s)
        for i in range(len(s)):
            if s[i] == ' ' or i == len(s) - 1:
                if end > 0:
                    if i == len(s) - 1:
                        end = i
                    self.copy(s, start, end)
                start = end = -1
            elif s[i] != ' ':
                if end < 0:
                    start = end = i
                else:
                    end = i
        return ''.join(s)


sol = Solution()
print(sol.reverseWords("I love u"))
print(sol.reverseWords("take"))
print(sol.reverseWords("Let's take LeetCode contest"))
