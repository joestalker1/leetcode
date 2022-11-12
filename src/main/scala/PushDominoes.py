class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        # assert self._pushDominoes('.L.R...LR..L..') == 'LL.RR.LLRRLL..','test1'
        # assert self._pushDominoes('RR.L') == 'RR.L','test2'
        return self._pushDominoes(dominoes)

    def _pushDominoes(self, dominoes: str) -> str:
        if not dominoes:
            return ''
        cmp = lambda x, y: 0 if x == y else (1 if x > y else 2)
        borders = [(i, ch) for i, ch in enumerate(dominoes) if ch != '.']
        borders = [(-1, 'L')] + borders + [(len(dominoes), 'R')]
        pushed = list(dominoes)
        for (i, left_ch), (j, right_ch) in zip(borders, borders[1:]):
            if left_ch == right_ch:
                for k in range(i + 1, j):
                    pushed[k] = left_ch
            # RL
            elif left_ch > right_ch:
                for k in range(i + 1, j):
                    pushed[k] = '.LR'[cmp((k - i), (j - k))]
        return ''.join(pushed)