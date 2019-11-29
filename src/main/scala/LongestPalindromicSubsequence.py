class Solution(object):
    def longestPalindromeSubseq(self, s):
        if not s:
            return 0
        max_len = 0
        for center in range(2*len(s) - 1):
            left = center // 2
            right = left + center % 2
            while left >= 0 and right < len(s) and s[left] == s[right]:
                max_len = max(max_len, right - left + 1)
                left -= 1
                right += 1
        return max_len
