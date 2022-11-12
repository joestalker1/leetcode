class Solution:
    def stoneGameIX(self, stones) -> bool:
        # assert self._stoneGameIX([7,10,1,9,19,17,1,9,19]) == True, 'test1'
        # assert self._stoneGameIX([2,3]) == False, 'test2'
        # assert self._stoneGameIX([20,3,20,17,2,12,15,17,4]) == True, 'test3'
        return self._stoneGameIX(stones)

    def _stoneGameIX(self, stones: List[int]) -> bool:
        if not stones:
            return False
        # alice wins: number of 1 - number of 2 > 2, if number of 1/2 >3 and flip is True.
        cnt_mod = [0] * 3
        for stone in stones:
            cnt_mod[stone % 3] += 1
        flip = (cnt_mod[0] % 2 != 0)
        if not cnt_mod[1]:
            return False if cnt_mod[2] < 3 else flip
        if not cnt_mod[2]:
            return False if cnt_mod[1] < 3 else flip
        if abs(cnt_mod[1] - cnt_mod[2]) > 2:
            return True
        return not flip
