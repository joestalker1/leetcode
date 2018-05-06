class Solution:
    def selfDividingNumbers(self, left, right):
        res = []
        for a in range(left, right + 1):
            v = a
            while v > 0:
                d = v % 10
                if d != 0 and a % d == 0:
                    v = v // 10
                else:
                    break
            if v == 0:
                res.append(a)
        return res


res = Solution()
print(res.selfDividingNumbers(1, 22))
