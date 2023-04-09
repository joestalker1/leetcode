class Solution:
    def canJump(self, nums) -> bool:
        # assert self._canJump([2,3,1,1,4]) == True, 'test1'
        # assert self._canJump([3,2,1,0,4]) == False, 'test2'
        # assert self._canJump([1,0,1,0]) == False, 'test3'
        return self._canJump(nums)

    def _canJump(self, nums):
        max_jump = 0
        for i, jump in enumerate(nums):
            if i > max_jump:
                return False
            max_jump = max(max_jump, i + jump)
        return True