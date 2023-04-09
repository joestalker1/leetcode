from collections import Counter

class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        if not word:
            return 0
        vowels = set(['a', 'e', 'i', 'o','u'])
        total_cnt = 0
        j = 0
        freq = Counter()

        def count_substr(freq, s, e):
            l = s
            while e > l and word[e] not in vowels:
                e -= 1
            cnt = 0
            while l < e and len(freq) == len(vowels):
                r = e
                freq1 = Counter(freq)
                while r > l and len(freq1) == len(vowels):
                    cnt += 1
                    freq1[word[r]] -= 1
                    if freq1[word[r]] == 0:
                        del freq1[word[r]]
                    r -= 1
                freq[word[l]] -= 1
                if freq[word[l]] == 0:
                    del freq[word[l]]
                l += 1
            return cnt


        for i in range(len(word)):
            if word[i] in vowels:
                freq[word[i]] += 1
            else:
                #count the vowel words
                if len(vowels) == len(freq):
                    total_cnt += count_substr(freq,j, i)
                j = i + 1
                freq = Counter()
        if len(vowels) == len(freq):
            total_cnt += count_substr(freq,j, i)
        return total_cnt


sol = Solution()
print(sol.countVowelSubstrings("ragvjaoeaieauuaaeaiii"))#18
print(sol.countVowelSubstrings("poazaeuioauoiioaouuouaui"))#31
print(sol.countVowelSubstrings("bbaeixoubb"))#0
print(sol.countVowelSubstrings("cuaieuouac"))#7