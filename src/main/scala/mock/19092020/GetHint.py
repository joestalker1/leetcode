from collections import Counter


class Solution:
    def getHint(self, secret, guess):
        if secret == guess:
            return str(len(secret)) + 'A0B'
        bulls = 0
        cows = 0
        freq = Counter(secret)
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
                freq[secret[i]] -= 1
        for i in range(len(secret)):
            if guess[i] in freq and freq[guess[i]] > 0:
                freq[guess[i]] -= 1
                cows += 1

        return str(bulls) + 'A' + str(cows) + 'B'

sol = Solution()
print
