class Solution:
    def chalkReplacer(self, chalk, k: int):
        if not chalk:
            return None
        req_chalk = sum(chalk)
        r = k % req_chalk
        i = 0
        while r:
            r -= chalk[i]
            if r < 0:
                return i
            i += 1
        return i
