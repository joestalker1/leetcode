class Solution:
    def findWords(self, words):
        s1 = "qwertyuiop"
        s2 = "asdfghjkl"
        s3 = "zxcvbnm"
        kb = {}
        for ch in s1:
            kb[ch] = 1

        for ch in s2:
            kb[ch] = 2

        for ch in s3:
            kb[ch] = 3
        res = []
        for word in words:
            c = 0
            for ch in word:
                ch1 = ch.lower()
                if c == 0:
                    c = kb[ch1]
                else:
                    c1 = kb[ch1]
                    if c != c1:
                        c = -1
                        break

            if c != -1:
                res.append(word)
        return res

sol = Solution()
print(sol.findWords(["Hello", "Alaska", "Dad", "Peace"]))