from collections import defaultdict

class DisjointSet:
    def __init__(self, words, n):
        self.sets = {word: word for word in words}
        self.sizes = {word: 1 for word in words}

    def union(self, x, y):
        synonyms = defaultdict(set)

        x, y = self.find(x), self.find(y)
        if x != y:
            if self.sizes[x] < self.sizes[y]: # union by size
                x, y = y, x
            self.sets[y] = x
            self.sizes[x] += self.sizes[y]

    def find(self, x):
        group = self.sets[x]

        while group != self.sets[group]:
            group = self.sets[group]
        self.sets[x] = group # path compression

        return group


def create_map(pairs):
    words = set(sum(pairs, ()))
    n = len(words)

    synonyms = DisjointSet(words, n)

    for x, y in pairs:
        synonyms.union(x, y)

    return synonyms.sets


def compare(s1, s2, pairs):
    synonyms = create_map(pairs)

    w1 = s1.split(); w2 = s2.split()

    for x, y in zip(w1, w2):
        if x == y:
            continue
        elif x in synonyms and y in synonyms and synonyms[x] == synonyms[y]:
            continue
        else:
            return False

    return True

print(compare("aaaa", "bbbbb", [('big', 'large'), ('eat', 'consume'), ('consume', 'ingest')]))

