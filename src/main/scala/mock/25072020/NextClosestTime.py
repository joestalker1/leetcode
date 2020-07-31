class Solution:
    def nextClosestTime(self, time):
        if not time:
            return time

        cur = 60 * int(time[0:2]) + int(time[3:])
        allowed = {int(c) for c in time if c != ':'}

        while True:
            cur = (cur + 1) % (24 * 60)
            digits = [cur // 60 // 10, cur // 60 % 10, cur % 60 // 10, cur % 60 % 10]
            for digit in digits:
                if all(digit in allowed for digit in digits):
                    return '{}{}:{}{}'.format(digits[0], digits[1], digits[2], digits[3])


sol = Solution()
print(sol.nextClosestTime("23:59"))
print(sol.nextClosestTime("19:34"))
