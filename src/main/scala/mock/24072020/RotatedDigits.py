class Solution:
    def rotatedDigits(self, N: int):
        valid = 0
        nums = set([2,5,6,9])
        bad_nums = set([3,4,7])
        for a in range(1, N+1):
            if a in nums:
                valid += 1
            else:
                rot = True
                changed = False
                while a > 0:
                    b = a % 10
                    if b in nums:
                        changed = True
                    if b in bad_nums:
                        rot = False
                        break
                    a = a // 10
                if rot and changed:
                    valid += 1
        return valid

sol = Solution()
print(sol.rotatedDigits(857))
print(sol.rotatedDigits(13))