class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
            op = 0
            x = target
            # go back : divide by 2 and add 1
            while x > startValue:
                if x % 2 == 0:
                    x //= 2
                else:
                    x += 1
                op += 1
            return op + startValue - x
