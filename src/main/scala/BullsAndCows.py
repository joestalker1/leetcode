from collections import defaultdict

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        h = defaultdict(int)
        bulls = cows = 0

        for idx, s in enumerate(secret):
            #
            g = guess[idx]
            if s == g:
                bulls += 1
            else:
                # bool expression is true, it's converted to int 1
                cows += int(h[s] < 0) + int(h[g] > 0)
                # if g is in secret, (h[g] > 0)
                h[s] += 1
                # if g is in secret and in guess, so it's cow
                h[g] -= 1

        return "{}A{}B".format(bulls, cows)
