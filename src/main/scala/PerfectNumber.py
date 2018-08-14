class Solution:
    def checkPerfectNumber(self, num):
        if num <= 1:
            return False
        sum = 0
        i = 1
        while i*i <= num:
            if num % i == 0:
                sum += i
                if i != 1:
                    sum += num // i
            i += 1
        return sum == num


sol = Solution()
print(sol.checkPerfectNumber(-6))
print(sol.checkPerfectNumber(28))

