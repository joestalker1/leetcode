class Solution:
    def shiftingLetters(self, s: str, shifts) -> str:
        s = list(s)
        shift_cnt = [0] * (len(s)+1)
        for b,e,d in shifts:
            if d == 1:
                shift_cnt[b] += 1
                shift_cnt[e+1] += -1
            else:
                shift_cnt[b] += -1
                shift_cnt[e+1] += 1
        for i in range(1, len(shift_cnt)):
            shift_cnt[i] += shift_cnt[i-1]
        cnt = 0
        for i in range(len(s)):
            cnt = ((ord(s[i]) - ord('a') + shift_cnt[i]) % 26 + 26) % 26
            s[i] = chr(ord('a') + cnt)
        return ''.join(s)
