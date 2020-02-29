from collections import Counter


class Solution:
    def expressiveWords(self, S, words):
        chars = Counter(S)
        char_set = set(list(S))
        count = 0
        for word in words:
            word_char_set = set(list(word))
            if char_set != word_char_set:
                continue
            chars_in_word = Counter(word)
            next_word = False
            for c in word:
                if chars[c] > chars_in_word[c] and chars[c] < 3 or chars_in_word[c] > chars[c]:
                    next_word = True
                    break
            if next_word:
                continue
            count += 1
        return count


sol = Solution()
print(sol.expressiveWords("abcd", ["abc"]))


