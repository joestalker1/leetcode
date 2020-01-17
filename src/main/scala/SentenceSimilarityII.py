import itertools

class Solution:
    def areSentencesSimilarTwo(self, words1, words2, pairs):
        if not words1 and not words2:
            return True
        if not words1 or not words2 or len(words1) != len(words2):
            return False
        encoding = {}
        i = itertools.count()

        def find(par, x):
            if par[x] != x:
                par[x] = find(par, par[x])
            return par[x]

        def union(par, r, x1, x2):
            p1 = find(par, x1)
            p2 = find(par, x2)
            if p1 == p2:
                return
            if rank[p1] > rank[p2]:
                par[p2] = p1
            elif rank[p1] < rank[p2]:
                par[p1] = p2
            else:
                par[p1] = p2
                rank[p2] += 1
        parent = [i for i in range(2 * len(pairs))]
        rank = [0] * len(parent)

        for w1, w2 in pairs:
            if w1 not in encoding:
                encoding[w1] = next(i)
            if w2 not in encoding:
                encoding[w2] = next(i)
            union(parent, rank, encoding[w1], encoding[w2])
        return all(w1 == w2 or w1 in encoding and w2 in encoding and find(parent, encoding[w1]) == find(parent, encoding[w2]) for w1, w2 in zip(words1, words2))


sol = Solution()
print(sol.areSentencesSimilarTwo(['aaa'], ['aaa'], []))
print(sol.areSentencesSimilarTwo(["great", "acting", "skills"], ["fine", "drama", "talent"],
                                         [["great", "good"], ["fine", "good"], ["acting", "drama"],
                                          ["skills", "talent"]]))
