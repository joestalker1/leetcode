class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0
        freq = {}
        max_len = 0
        cur_len = 0
        for i in range(len(s)):
            if s[i] not in freq or freq[s[i]] == 0:
                freq[s[i]] = 1
                cur_len += 1
            else:
                j = i - cur_len
                while s[j] != s[i]:
                    freq[s[j]] -= 1
                    j += 1
                cur_len = i - j
            max_len = max(max_len, cur_len)
        return max_len


sol = Solution()
print(sol.lengthOfLongestSubstring("pwwkew"))#3
print(sol.lengthOfLongestSubstring("bbbbb"))#1
print(sol.lengthOfLongestSubstring("abcabcbb"))#3
