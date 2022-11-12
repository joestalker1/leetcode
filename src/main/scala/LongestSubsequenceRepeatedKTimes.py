from collections import Counter
from itertools import combinations,permutations

class Solution:
    def is_subseq(self, subseq,s):
        i = 0
        for c in subseq:
            i = s.find(c,i)
            if i == -1:
                return False
            i += 1
        return True
        #return all(c in it for c in subseq)

    def longestSubsequenceRepeatedK(self, s, k):
        char_freq = Counter(s)
        cand_chars = ''.join(ch * (freq//k) for ch,freq in char_freq.items())
        combs = set()
        for l in range(len(cand_chars) + 1):
            for comb in combinations(cand_chars, l):
                for perm in permutations(comb):
                    combs.add(''.join(perm))
        sorted_comb = sorted(combs, key=lambda x:[len(x),x],reverse=True)
        for comb in sorted_comb:
            if self.is_subseq(comb*k,s):
                return comb




