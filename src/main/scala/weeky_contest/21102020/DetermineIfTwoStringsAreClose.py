from collections import Counter

class Solution:
    def closeStrings(self, word1, word2):
        if len(word1) != len(word2):
            return False
        freq1 = Counter(word1)
        lst1 = [a for k,a in freq1.items()]
        freq2 = Counter(word2)
        lst2 = [a for k,a in freq2.items()]
        if set(freq1.keys()) != set(freq2.keys()):
            return False
        lst1.sort()
        lst2.sort()
        return lst1 == lst2


sol = Solution()
print(sol.closeStrings("abc", "dca"))








