class Solution:
    def minimumMoves(self, s: str) -> int:
        if not s:
            return s

        def count_moves(s):
            moves = 0
            cnt = 0
            l = 0
            for i in range(len(s)):
                if i - l + 1 == 3 or cnt == 3:
                    if cnt > 0:
                        moves += 1
                        cnt = 0
                        l = i + 1
                        continue
                if s[i] == 'X':
                    cnt += 1
                if cnt == 1 and s[i] == 'X':
                    l = i
            if cnt > 0:
                moves += 1
            return moves

        moves1 = count_moves(s)
        moves2 = count_moves(s[::-1])
        if moves1 == 0 and moves2 == 0:
            return moves1
        if moves1 != 0 and moves2 == 0:
            return moves1
        if moves1 == 0 and moves2 != 0:
            return moves2
        return min(moves1, moves2)



sol = Solution()
print(sol.minimumMoves("XXXOOXXX"))#2
print(sol.minimumMoves('OXOX'))#1
print(sol.minimumMoves("XOOX"))#2