from math import inf
from functools import lru_cache

class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        # assert self._earliestAndLatest(2,1,2) == [1,1], 'test1'
        # assert self._earliestAndLatest(3, 1, 2)== [2,2], 'test2'
        # assert self._earliestAndLatest(5, 1, 2)== [3,3], 'test3'
        return self._earliestAndLatest(n, firstPlayer, secondPlayer)

    def _earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        min_round = inf
        max_round = -inf

        @lru_cache(None)
        def play(dead, i, j, cur_round):
            nonlocal min_round, max_round
            if i >= j:
                play(dead, 1, n, cur_round + 1)
            elif (1 << i) & dead:
                # if i is dead,let take i + 1
                play(dead, i + 1, j, cur_round)
            elif (1 << j) & dead:
                # if j is dead,get next
                play(dead, i, j - 1, cur_round)
            elif i == firstPlayer and j == secondPlayer:
                min_round = min(min_round, cur_round)
                max_round = max(max_round, cur_round)
            else:
                # try 2 cases: make dead i and j
                if i != firstPlayer and i != secondPlayer:
                    play((1 << i) | dead, i + 1, j - 1, cur_round)
                if j != firstPlayer and j != secondPlayer:
                    play((1 << j) | dead, i + 1, j - 1, cur_round)

        play(0, 1, n, 1)
        return [min_round, max_round]
