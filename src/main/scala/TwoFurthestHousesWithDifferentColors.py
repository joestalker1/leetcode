class Solution:
    def maxDistance(self, colors) -> int:
        # assert self._maxDistance([1,1]) == 0,'test1'
        # assert self._maxDistance([1,2,1]) == 1,'test2'
        # assert self._maxDistance([1,2,1,2,2,2,2]) == 6,'test3'
        # assert self._maxDistance([1,2,2,2,2,2,2]) == 6 ,'test4'
        return self._maxDistance(colors)

    def _maxDistance(self, colors) -> int:
        if not colors:
            return 0
        last = len(colors) - 1
        while colors[0] == colors[last]:
            last -= 1
        first = 0
        while colors[-1] == colors[first]:
            first += 1
        return max(last, len(colors) - first - 1)