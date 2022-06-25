class Solution:
    def minimumDeletions(self, s: str) -> int:
        if not s:
            return 0
        cnt_a = 0
        cnt_b = 0
        dp = 0
        for i in range(len(s)):
            if s[i] == 'a':
                #1 remove all b before i to make s[0:i] being balanced
                #2 remove all whatever make s[0:i-1] balanced + one a
                dp = min(dp + 1, cnt_b)
            else:
                #nothing to add, just appenf b and s[0:i] has the same complexity as s[0:i-1]
                cnt_b += 1
        return dp