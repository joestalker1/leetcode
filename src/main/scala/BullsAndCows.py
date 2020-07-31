from collections import defaultdict

class Solution:
    def getHint(self, secret, guess):
        # count bulls
        bulls = 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1

        cows = 0
        char_pos = defaultdict(list)
        for i in range(len(guess)):
            char_pos[secret[i]].append(i)

        for i in range(len(secret)):
            if secret[i] != guess[i]:
                if guess[i] in char_pos and len(char_pos[guess[i]]) > 0:
                    cows += 1
                    char_pos[guess[i]].pop()
        return 'A{}B{}'.format(bulls, cows)
