class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        if len(s) == 1:
            return 0
        one_cnt = sum(1 for i in range(len(s)) if s[i] == '1')
        first_zero_pos = one_cnt
        left_pos = 0
        for i in range(len(s)):
            if s[i] == '0':
                left_pos = i
                break
        if first_zero_pos > left_pos:
            cnt = 0
            for i in range(left_pos + 1, len(s)):
                if s[i] == '1':
                    break
                cnt += 1
            first_zero_pos += cnt
        last_one_pos = one_cnt - 1
        right_pos = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '1':
                right_pos = i
                break
        #count 1 before the last 1
        if right_pos > last_one_pos:
            cnt = 0
            for i in range(right_pos - 1, -1, -1):
                if s[i] == '0':
                    break
                cnt += 1
            right_pos += cnt
        return max(first_zero_pos - left_pos,right_pos - last_one_pos)

sol = Solution()
print(sol.secondsToRemoveOccurrences("1001111111110001011001110000000110101"))#20