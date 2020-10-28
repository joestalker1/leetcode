from heapq import heappush, heappop

class Solution:
    def slidingPuzzle(self, board):
        num_to_pos = {1:[0,0],2:[0,1],3:[0,2],4:[1,0],5:[1,1]}

        def cost(num, r,c):
            r1,c1 = num_to_pos[num]
            return abs(r - r1) + abs(c - c1)

        cur_pos = []
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 0:
                    cur_pos = [r,c]
                    break
        q = [cur_pos]

        def solved():
            return all([i == board[i // 3][(i-1) % 3] for i in range(1, 6)])

        while q:
            r,c = heappop(q)

