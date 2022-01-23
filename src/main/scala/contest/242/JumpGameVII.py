class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        # assert self._canReach('',0,1)== False, 'empty string'
        # assert self._canReach('01110', 1, 2) == False, 'small jumps'
        # assert self._canReach('01110', 5,6) == False, 'greater jumps'
        return self._canReach(s, minJump, maxJump)

    def _canReach(self, s, minJump, maxJump):
        dp = [False] * len(s)
        dp[0] = True
        pre = 0
        for i in range(1, len(s)):
            if i - minJump >= 0 and dp[i - minJump]:
                pre += 1
            if i - maxJump > 0 and dp[i - maxJump - 1]:
                pre -= 1
            if pre > 0 and s[i] == '0':
                dp[i] = True
        return dp[-1]
