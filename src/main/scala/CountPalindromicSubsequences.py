class Solution:
    def countPalindromes(self, s: str) -> int:
        if not s:
            return 0
        MOD = 10 ** 9 + 7
        n = len(s)
        pre = [[[0] * 10 for _ in range(10)] for _ in range(n)]
        char_cnt = [0] * 10
        for i in range(n):
            c = ord(s[i]) - ord('0')
            if i > 0:
                for j in range(10):
                    for k in range(10):
                        pre[i][j][k] = pre[i-1][j][k]
                        if c == k:
                            pre[i][j][k] += char_cnt[j]
            char_cnt[c] += 1
        suf = [[[0] * 10 for _ in range(10)] for _ in range(n)]
        char_cnt = [0] * 10
        for i in range(n-1,-1,-1):
            c = ord(s[i]) - ord('0')
            if i < n - 1:
                for j in range(10):
                    for k in range(10):
                        suf[i][j][k] = suf[i+1][j][k]
                        if c == k:
                            suf[i][j][k] += char_cnt[j]
            char_cnt[c] += 1
        poly_cnt = 0
        for i in range(2,n-2):
            for j in range(10):
                for k in range(10):
                    poly_cnt += (pre[i-1][j][k] * suf[i+1][j][k]) % MOD
        return poly_cnt % MOD
    