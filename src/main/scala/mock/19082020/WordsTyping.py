class Solution:
    def wordsTyping(self, sentence, rows, cols):
        count = 0
        cur_word = 0
        for i in range(rows):
            j = 0
            while j < cols:
                l = sentence[cur_word]
                if j + l + 1 < cols:
                    j += (l + 1)  # add space between word
                    cur_word += 1
                else:
                    break
            if cur_word == len(sentence):
                count += 1
        return count
