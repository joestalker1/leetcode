class Solution:
    def wordsTyping(self, sentence, rows, cols):
        s = ' '.join(sentence) + ' '
        # size of tied string
        sz = len(s)
        pos = 0 # where finish sentence in screen
        for i in range(rows):
            pos += cols
            # check if it doesn't finish inside some word
            if s[pos % sz] == ' ':
                # calculate new position
                pos += 1
                continue
            pos_in_s = (pos-1) % sz
            while pos >= 0 and s[(pos-1) % sz] != ' ':
                pos_in_s = (pos - 1) % sz
                pos -= 1
        return pos // sz


sol = Solution()
#print(sol.wordsTyping(["f", "p", "a"], 8, 7))  # 10
#print(sol.wordsTyping(["a"], 10000, 10000))#50000000
# print(sol.wordsTyping(rows = 4, cols = 5, sentence = ["I", "had", "apple", "pie"]))#1
print(sol.wordsTyping(rows=3, cols=6, sentence=["a", "bcd", "e"]))  # 2
#print(sol.wordsTyping(rows=2, cols=8, sentence=["hello", "world"]))  # 1
