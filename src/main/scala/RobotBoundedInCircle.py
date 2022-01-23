class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # assert self._isRobotBounded('G') == False, 'direct path'
        # assert self._isRobotBounded('GL') == True, 'left cycle'
        # assert self._isRobotBounded('GR') == True, 'right cycle'
        # assert self._isRobotBounded('L') == True,'standing'
        return self._isRobotBounded(instructions)

    def _isRobotBounded(self, instructions: str) -> bool:
        x = 0
        y = 0
        dx = 0
        dy = 1
        # norht,east,south,west
        steps = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        #
        idx = 0
        # after 4 cycles we should come back to original position
        for _ in range(4):
            for instruction in instructions:
                if instruction == 'L':
                    idx = (idx + 3) % 4
                    dx, dy = steps[idx]
                elif instruction == 'R':
                    idx = (idx + 1) % 4
                    dx, dy = steps[idx]
                else:
                    x += dx
                    y += dy
        return x == 0 and y == 0