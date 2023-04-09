class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        if not word:
            return 0
        vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
        total_cnt = 0
        j = k = vow = 0
        for i in range(len(word)):
            if word[i] in vowels:
                vowels[word[i]] += 1
                if vowels[word[i]] == 1:
                    vow += 1
                while vow == 5:
                    if word[k] in vowels:
                        vowels[word[k]] -= 1
                        if vowels[word[k]] == 0:
                            vow -= 1
                    k += 1
                total_cnt += k - j
            else:
                vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
                vow = 0
                j = k = i + 1
        return total_cnt