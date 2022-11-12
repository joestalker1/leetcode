from collections import Counter

class Solution:
    def longestPalindrome(self, words) -> int:
        # assert self._longestPalindrome(["em","pe","mp","ee","pp","me","ep","em","em","me"]) == 14, 'test1'
        return self._longestPalindrome(words)

    def _longestPalindrome(self, words) -> int:
        if not words:
            return 0
        long_poly_len = 0
        word_freq = Counter(words)
        central = False
        for word in word_freq:
            reversed_word = word[::-1]
            if word[0] == word[1]:
                if word_freq[word] % 2 == 0:
                    long_poly_len += word_freq[word]
                else:
                    long_poly_len += word_freq[word] - 1
                    central = True
            elif word[0] < word[1]:  # such way we count word and reversed word one time!
                min_freq = min(word_freq[word], word_freq[reversed_word])
                long_poly_len += 2 * min_freq
        long_poly_len += 1 if central else 0
        return long_poly_len * 2