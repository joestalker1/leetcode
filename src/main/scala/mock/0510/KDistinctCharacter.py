from collections import defaultdict

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s, k):
        if not s or k == 0:
            return 0
        chars = defaultdict(lambda: 0)
        i = 0
        j = 0
        max_len = 0
        while i <= j:
            if j < len(s):
                chars[s[j]] += 1
                j += 1
                while len(chars.keys()) > k and i < len(s) and i <= j:
                    chars[s[i]] -= 1
                    if chars[s[i]] == 0:
                        del chars[s[i]]
                    i += 1
                max_len = max(max_len, j - i)
            else:
                break
        return max_len


sol = Solution()
print(sol.lengthOfLongestSubstringKDistinct(s = "aa", k = 1))
print(sol.lengthOfLongestSubstringKDistinct(s = "eceba", k = 2))


