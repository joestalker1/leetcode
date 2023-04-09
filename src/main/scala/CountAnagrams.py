from collections import Counter

class Solution:
    def countAnagrams(self, s):
        # assert self._countAnagrams('too hot') == 18,'test1'
        # assert self._countAnagrams('ta aa') == 2,'test2'
        return self._countAnagrams(s)

    def _countAnagrams(self, s: str) -> int:
        if not s:
            return 0
        MOD = 10 ** 9 + 7

        def mul_mod(a, b):
            return (a % MOD * b % MOD) % MOD

        def bin_exp(a, n):
            if n == 0:
                return 1
            res = bin_exp(a, n // 2)
            if n & 1:
                return mul_mod(a, mul_mod(res, res))
            else:
                return mul_mod(res, res)

        def mod_inv(a):
            return bin_exp(a, MOD - 2)

        words = s.split()
        max_len = len(max(words, key=lambda x: len(x)))
        fact = [1] * (max_len + 1)
        for i in range(2, len(fact)):
            fact[i] = mul_mod(fact[i - 1], i)
        word_perm = 1
        for word in words:
            freq = Counter(word)
            uniq_cnt = fact[len(word)]
            rep_cnt = 1
            for k in freq:
                if freq[k] > 1:
                    rep_cnt = mul_mod(rep_cnt, fact[freq[k]])

            word_perm = mul_mod(word_perm, mul_mod(uniq_cnt, mod_inv(rep_cnt)))
        return word_perm