# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):
def guess(num):
    if num == 5:
        return 0
    if num < 5:
        return 1
    return -1


class Solution(object):
    def guessNumber(self, n):
        i = 1
        j = n
        while i < j:
            num = i + (j - i) // 2
            guess_res = guess(num)
            if not guess_res:
                return num
            if guess_res < 0:
                j = num
            else:
                i = num + 1
        return i


sol = Solution()
print(sol.guessNumber(5))