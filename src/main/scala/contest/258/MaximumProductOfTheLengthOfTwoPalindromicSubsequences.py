from collections import defaultdict,Counter
from math import inf

class Solution:
    def maxProduct(self, s: str) -> int:
        if not s:
            return 0

        def find_freq(s, l, r):
            freq = defaultdict(list)
            for i in range(l,r+1):
                freq[s[i]].append(i)
            return freq

        def find_count(freq,ch, l, r):
            cnt = 0
            for i in freq[ch]:
                if l <= i <= r:
                    cnt += 1
            return cnt

        def find_max_poly_len(freq,ch):
            l = freq[ch][0]
            r = freq[ch][-1]
            cur_len = len(freq[ch])
            max_cnt = -inf
            best_ch = None
            for ch2 in freq:
                len_of_ch2 = find_count(freq,ch2,l, r)
                if ch2 == ch or len_of_ch2 < 1:
                    continue
                if cur_len % 2 == 1 and len_of_ch2 % 2 == 0 and max_cnt < len_of_ch2:
                    max_cnt = len_of_ch2
                    best_ch = ch2
                elif cur_len % 2 == 0 and max_cnt < len_of_ch2:
                    max_cnt = len_of_ch2
                    best_ch = ch2
            while best_ch and freq[best_ch] and l <= freq[best_ch][0] <= r:
                freq[best_ch].pop(0)
            return cur_len + (max_cnt if max_cnt != -inf else 0)

        max_prod = -inf
        for ch1 in list(set(s)):
            freq = find_freq(s,0,len(s) - 1)
            if len(freq[ch1]) < 2:
                continue
            poly1 = find_max_poly_len(freq, ch1)
            freq[ch1] = []
            for ch2 in freq:
                cur_len = find_count(freq,ch2,0,len(s) - 1)
                if ch2 == ch1 or cur_len < 2:
                    continue
                poly2 = find_max_poly_len(freq,ch2)
                max_prod = max(max_prod, poly1 * poly2)
        return max_prod


sol = Solution()
print(sol.maxProduct("accbcaxxcxx"))