class Solution:
    def longestPalindrome(self, s):
        if len(s) == 0:
            return 0

        dict1 = {}
        for ch in s:
            if ch in dict1:
                c = dict1[ch]
                dict1[ch] = c + 1
            else:
                dict1[ch] = 1
        len1 = 0
        odd_len = 0
        key = 0
        for k, v in dict1.items():
            if v > 0 and (v & 1) == 0:
                len1 += v
                dict1[k] = 0
            elif v > 0 and (v & 1) == 1:
                if v > odd_len:
                    odd_len = v
                    key = k
        len1 += odd_len
        for k, v in dict1.items():
            if v > 0 and (k != key) and (v & 1) == 1:
                v -= 1
                if v > 0:
                    len1 += v
        return len1


sol = Solution()
print(sol.longestPalindrome("abccccdd"))