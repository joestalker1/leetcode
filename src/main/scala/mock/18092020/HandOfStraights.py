from collections import Counter

class Solution:
    def isNStraightHand(self, hand, W):
        freq = Counter(hand)
        while freq:
            # find min number
            m = min(freq)
            # try ti build subsequence m,m+1,... by W-length
            for b in range(m, m + W):
                if b not in freq:
                    return False
                v = freq[b]
                if v == 1:
                    del freq[b]
                else:
                    freq[b] -= 1
        return True

