class Solution:
    def numberOfSteps (self, num: int):
        if num == 0:
            return 0

        a = num
        steps = 0
        while a > 0:
            if a & 1 == 0:
                #number is even
                a = a >> 1
            else:
                a -= 1
            steps += 1
        return steps


sol = Solution()
print(sol.numberOfSteps(14))

