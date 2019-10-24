class Solution:
    def isAlienSorted(self, words, order):
        if not words or not order:
            return False
        map = {char: i for i,char in enumerate(order)}
        new_words = []
        for word in words:
            new_word = [map[ch] for ch in word]
            new_words.append(new_word)
        for i in range(1, len(new_words)):
            if new_words[i-1] > new_words[i]:
                return False
        return True

sol = Solution()
print(sol.isAlienSorted(words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"))
print(sol.isAlienSorted(words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"))
print(sol.isAlienSorted(words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"))




