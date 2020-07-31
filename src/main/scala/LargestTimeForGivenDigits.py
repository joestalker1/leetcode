class Solution:
    def largestTimeFromDigits(self, A):

        def gen_time(digits, start):
            if start == 4:
                h = 10*digits[0] + digits[1]
                m = 10*digits[2] + digits[3]
                if 0 <= h<24 and 0 <= m < 60:
                    return digits[::]
                return None
            for i in range(4):
                digits[start],digits[i] = digits[i],digits[start]
                fit_time = gen_time(digits,start + 1)
                if fit_time:
                    return fit_time
                digits[start],digits[i] = digits[i],digits[start]
            return None
        ans = gen_time(A, 0)
        if ans:
            return "{}{}:{}{}".format(ans[0],ans[1],ans[2],ans[3])
        return ""


sol = Solution()
print(sol.largestTimeFromDigits([1,2,3,4]))