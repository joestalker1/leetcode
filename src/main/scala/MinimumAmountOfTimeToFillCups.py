class Solution:
    def fillCups(self, amount: List[int]) -> int:
        # assert self._fillCups([1,1,1]) == 1, 'test1'
        # assert self._fillCups([1,2,1]) == 2, 'test3'
        # assert self._fillCups([3,0,0]) == 3, 'test4'
        # assert self._fillCups([3,4,0]) == 4, 'test5'
        # assert self._fillCups([3,4,4]) == 6, 'test6'
        return self._fillCups(amount)

    def _fillCups(self, amount: List[int]) -> int:
        min_time = 0
        while (amount[0] + amount[1]) > 0:
            #inline sort
            amount.sort()
            amount[1] -= 1
            amount[2] -= 1
            min_time += 1
        return min_time + amount[-1]