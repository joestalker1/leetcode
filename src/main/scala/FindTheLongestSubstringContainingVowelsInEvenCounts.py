class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        pr = defaultdict(int)
        chars = set('aeiou')
        pr[0] = -1
        cur_mask = 0
        max_len = 0
        for i,ch in enumerate(s):
            if ch in chars:
                cur_mask ^= 1 << (ord(ch) - ord('a'))
            if cur_mask in pr:
                max_len = max(max_len, i - pr[cur_mask])
            else:
                pr[cur_mask] = i
        return max_len 