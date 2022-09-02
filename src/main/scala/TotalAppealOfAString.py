class Solution:
    def appealSum(self, s: str) -> int:
        if not s:
            return 0
        cur_num = 0
        show_last_pos = [0] * 27
        res = 0
        for i in range(len(s)):
            code = ord(s[i]) - ord('a')
            #add char to all string between previous char and current and number distinct chars are i - show_last_pos[code] + 1
            cur_num += i - show_last_pos[code] + 1
            show_last_pos[code] = i + 1
            res += cur_num
        return res
