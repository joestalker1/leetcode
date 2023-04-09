from collections import Counter,defaultdict


class Solution:
    def findSubstring(self, s: str, words):
        if not s or not words:
            return []
        uniq_words = Counter(words)
        starts = []
        one_word_len = len(words[0])
        need_len = len(words) * one_word_len

        def sliding_window(i):
            words_found = defaultdict(int)
            words_used = 0
            excess_word = False
            for j in range(i, len(s), one_word_len):
                if j + one_word_len > len(s):
                    break
                sub = s[j:j + one_word_len]
                if sub not in uniq_words:
                    words_found = defaultdict(int)
                    words_used = 0
                    excess_word = False
                    i = j + one_word_len
                else:
                    while j - i == need_len or excess_word:
                        word = s[i:i+one_word_len]
                        i += one_word_len
                        words_found[word] -= 1
                        if words_found[word] == uniq_words[word]:
                            excess_word= False
                        else:
                            words_used -= 1
                    words_found[sub] += 1
                    if words_found[sub] <= uniq_words[sub]:
                        words_used += 1
                    else:
                        excess_word = True
                    if words_used == len(words) and not excess_word:
                        starts.append(i)
        for k in range(one_word_len):
            sliding_window(k)
        return starts