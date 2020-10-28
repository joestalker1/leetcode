from collections import defaultdict

class Solution:
    def alphabetBoardPath(self, target):
        if not target:
            return ''
        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
        char_to_pos = defaultdict(list)
        for r in range(len(board) - 1):
            for c in range(len(board[0])):
                ch = board[r][c]
                char_to_pos[ch] = [r,c]
        char_to_pos['z'] = [len(board) - 1, 0]
        res = []
        cur_pos = [0, 0]
        i = 0
        while i < len(target):
            ch = target[i]
            r,c = char_to_pos[ch]
            dr = r - cur_pos[0]
            dc = c - cur_pos[1]
            if dr > 0:
                if abs(dr) == 5 and c == 0:
                    # go down
                    res.append('D' * dr)
                else:
                    dr = 4
                    res.append('D' * dr)
            elif dr < 0:
                # go up
                res.append('U' * abs(dr))
            if dc < 0:
                # go to the left
                res.append('L' * abs(dc))
            elif dc > 0:
                # go to the right
                res.append('R' * dc)
            if cur_pos[0] + dr == r and cur_pos[1] + dc == c:
                cur_pos = [r,c]
                res.append('!')
                i += 1
            else:
                cur_pos = [cur_pos[0] + dr, cur_pos[1] + dc]
        return ''.join(res)

#"DDDDD!UUUUURRR!DDDDLLLD!"
# DDDDD!UUUUURRR!DDDDDLLL!
sol = Solution()
print(sol.alphabetBoardPath("zdz"))




