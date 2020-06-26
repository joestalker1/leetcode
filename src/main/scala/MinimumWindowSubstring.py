from collections import Counter
from collections import defaultdict


class Solution:
    def minWindow(self, s, t):
        if not s and not t:
            return t
        if not s or not t:
            return ""
        min_win = [float('inf'), None, None]
        chars = Counter(t)
        need = len(chars)
        win = defaultdict(int)
        left = 0
        formed = 0
        for right in range(len(s)):
            ch = s[right]
            win[ch] += 1
            if ch in chars and win[ch] == chars[ch]:
                formed += 1
            while left <= right and formed == need:
                if min_win[0] > right - left + 1:
                    min_win = [right - left + 1, left, right]
                win[s[left]] -= 1
                if s[left] in chars and win[s[left]] < chars[s[left]]:
                    formed -= 1
                left += 1
        formed, l, r = min_win
        return s[l: r + 1] if formed != float('inf') else ''


sol = Solution()
print(sol.minWindow("aa", "aa"))
print(sol.minWindow("bdab", "ab"))
print(sol.minWindow("a", "aa"))
print(sol.minWindow("ADOBECODEBANC", "ABC"))
