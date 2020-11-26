import collections

class Solution:
    def gcd(self, a, b):
        if b ==0:
            return a
        return self.gcd(b, a % b)

    def hasGroupsSizeX(self, deck):
        if len(deck) < 2:
            return False
        groups = collections.Counter(deck)
        g = -1
        for c in groups.values():
            if g == -1:
                g = c
            else:
                g = self.gcd(g, c)
        return g >= 2
