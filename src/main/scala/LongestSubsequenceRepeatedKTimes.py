from collections import Counter
from itertools import combinations,permutations

class Solution:
    def is_subseq(self, s, t):
        it = iter(t)
        return all(c in it for c in s)

    def longestSubsequenceRepeatedK(self, s, k):
        hot = ''.join(ch * (freq//k) for ch,freq in Counter(s).items())
        combs = set()
        for l in range(len(hot) + 1):
            for comb in combinations(hot, l):
                for perm in permutations(comb):
                    combs.add(''.join(perm))
        sorted_cand =sorted(combs, key=lambda x:(len(x),x),reverse=True)
        for cand in sorted_cand:
            if self.is_subseq(cand * k, s):
                return cand




