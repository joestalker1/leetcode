from collections import defaultdict
from heapq import heappop, heappush


class Solution:
    def topNWords(self, numToys, topToys, toys, numQuotes, quotes):
        if topToys > numToys:
            quote_words = {w: True for quote in quotes for w in quote.split(' ')}
            res = [w for w in toys if w in quote_words]
            res.sort()
            return res
        else:
            words = set(toys)
            word_to_freq = defaultdict(lambda :0)
            for quote in quotes:
                for w in quote.split(' '):
                    if w.lower() in words:
                        word_to_freq[w.lower()] += 1
            word_freq = word_to_freq[toys[0]]
            if len(toys) == sum([1 for w, f in word_to_freq.items() if f == word_freq]):
                res = word_to_freq.keys()
                res.sort()
                return res
            freq = []
            for w, f in word_to_freq.items():
                if len(freq) < topToys:
                    heappush(freq, [f, w])
                else:
                    if freq[0][0] < f:
                        heappop(freq)
                        heappush(freq, [f, w])
            res = []
            while len(freq):
                f, word = heappop(freq)
                res.append(word)
            return res[::-1]


sol = Solution()
print(sol.topNWords(numToys=6,
                    topToys=2,
                    toys=["elmo", "elsa", "legos", "drone", "tablet", "warcraft"],
                    numQuotes=6,
                    quotes=[
                        "Elmo is the hottest of the season! Elmo will be on every kid's wishlist!",
                        "The new Elmo dolls are super high quality",
                        "Expect the Elsa dolls to be very popular this year, Elsa!",
                        "Elsa and Elmo are the toys I'll be buying for my kids, Elsa is good",
                        "For parents of older kids, look into buying them a drone",
                        "Warcraft is slowly rising in popularity ahead of the holiday season"
                    ]))
