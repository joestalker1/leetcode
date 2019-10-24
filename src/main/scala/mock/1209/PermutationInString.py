from collections import Counter

class Solution:
    def checkInclusion(self, s1, s2):
        if not s1 or not s2:
            return False
        substr = Counter(s1)
        word = Counter()
        for i in range(len(s2)):
            if substr == word:
                return True
            if sum(word.values()) >= len(s1):
                j = i - len(s1)
                word[s2[j]] -= 1
                if word[s2[j]] == 0:
                    word.pop(s2[j], None)
            word[s2[i]] += 1

        return substr == word

sol = Solution()
print(sol.checkInclusion("adc", "dcda"))#true
print(sol.checkInclusion(s1 = "ab", s2 = "baooo"))

