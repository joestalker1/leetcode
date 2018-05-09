class Solution:
    def findTheDifference(self, s, t):
        if len(s) == 0:
            return ""
        if len(t) == 0:
            return ""
        chars = {}
        for ch in s:
            if ch in chars:
                d = chars[ch]
                chars[ch] = d + 1
            else:
                chars[ch] = 1
        list1 = []
        for ch in t:
            if ch in chars:
                c = chars[ch]
                if c == 0:
                   list1.append(ch)
                else:
                    chars[ch] = c - 1
            else:
                list1.append(ch)
        return list1[0]

sol = Solution()
print(sol.findTheDifference("abcd", "abcde"))