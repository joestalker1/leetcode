class Solution(object):
    def minTimeToType(self, word):
        last_ch = 'a'
        time = 0
        d = ord('z') - ord('a')
        for ch in word:
            if last_ch == ch:
                time += 1
            else:
                if ord(ch) > ord(last_ch):
                    # clockwise:
                    move_clockwise = ord(ch) - ord(last_ch)
                    # counter_clockwise
                    move_counterclockwise = d - move_clockwise + 1
                else:
                    move_counterclockwise = ord(last_ch) - ord(ch)
                    # clockwise: ch < last_ch
                    move_clockwise = ord(ch) - ord('a') + ord('z') - ord(last_ch) + 1
                time += min(move_counterclockwise + 1, move_clockwise + 1)
            last_ch = ch
        return time

sol = Solution()
print(sol.minTimeToType("bza"))#7
print(sol.minTimeToType("abc"))#5


