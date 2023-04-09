class Solution:
    def countVowels(self, word: str) -> int:
        # assert self._countVowels('aba') == 6,'test1'
        # assert self._countVowels('ddd') == 0,'test2'
        # assert self._countVowels('abc') == 1,'test3'
        return self._countVowels(word)

    def _countVowels(self, word: str) -> int:
        if not word:
            return 0
        MOD = 10 ** 9 + 7
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        sum_of_vowels = 0
        for i in range(len(word)):
            if word[i] in vowels:
                sum_of_vowels += (i + 1) * (len(word) - i)
        return sum_of_vowels