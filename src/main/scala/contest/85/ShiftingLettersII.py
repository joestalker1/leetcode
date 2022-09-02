class Solution:
    def shiftingLetters(self, s: str, shifts) -> str:
        lst = list(s)
        op_cnt = [0] * len(s)

        for start, end, direct in shifts:
             for k in range(start, end + 1):
                 if direct == 0:
                     op_cnt[k] -= 1
                 else:
                     op_cnt[k] += 1

        def code(ch):
            return ord(ch) - ord('a')

        for i in range(len(lst)):
            if op_cnt[i] == 0:
                continue
            d = op_cnt[i]
            if d > 0:
                lst[i] = chr(ord('a') + (code(lst[i]) + d) % 26)
            elif d < 0:
                lst[i] = chr(ord('a') + (code(lst[i]) - d + 26) % 26)

        return ''.join(lst)


sol = Solution()
print(sol.shiftingLetters("dztz", [[0,0,0],[1,1,1]]))
