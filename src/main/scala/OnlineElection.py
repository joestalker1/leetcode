import bisect
import collections

class TopVotedCandidate(object):
    def __init__(self, persons, times):
        self.count = collections.defaultdict(int)
        self.winner = []
        c = 0
        for t, p in zip(times, persons):
            self.count[p] += 1
            if self.count[p] >= c:
                self.winner.append((t, p))
            c = max(c, self.count[p])

    def q(self, t):
        j = bisect.bisect(self.winner, (t, float('inf')))
        return self.winner[j - 1][1]