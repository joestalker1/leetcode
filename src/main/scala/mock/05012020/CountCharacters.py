from collections import Counter,defaultdict

class Solution:
    def countCharacters(self, words, chars):
        if not words:
            return 0
        if not chars:
            return sum(map(lambda s: len(s), words))
        allowed_chars = Counter(list(chars))
        total_len = 0
        for word in words:
            freq = defaultdict(int)
            permit = True
            for ch in word:
                freq[ch] += 1
                if ch not in allowed_chars or freq[ch] > allowed_chars[ch]:
                    permit = False
                    break
            if permit:
                total_len += len(word)
        return total_len


sol = Solution()
print(sol.countCharacters(words = ["cat","bt","hat","tree"], chars = "atach"))

