class Solution:
    def longestBeautifulSubstring(self, word: str):
        #vowels ('a', 'e', 'i', 'o', 'u')
        vowels = {'a':1, 'e':2, 'i':3, 'o':4, 'u':5}
        seen = set()
        seen.add(word[0])
        l = 0
        max_len = 1
        last_ch = word[0]
        for r in range(1, len(word)):
            if word[r] not in vowels or vowels[last_ch] > vowels[word[r]]:
                last_ch = word[r]
                l = r
                seen.clear()
            else:
                last_ch = word[r]
                seen.add(last_ch)
                if len(seen) == len(vowels):
                    max_len = max(max_len,r - l + 1)
        return max_len


