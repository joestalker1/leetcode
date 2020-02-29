class Solution:
    def to_int(self, arr):
        k = 1
        n = 0
        for i in range(len(arr) - 1, -1, -1):
            n += arr[i] * k
            k *= 10
        return n

    def nextGreaterElement(self, n):
        if not n:
            return -1
        max_n = 2 ** 31 - 1
        digits = []
        while n > 0:
            d = n % 10
            digits.insert(0, d)
            n = n // 10
        p = -1
        i = len(digits) - 1
        while i > 0 and p == -1:
            if digits[i] > digits[i-1]:
                p = i - 1
                break
            i -= 1
        if p == -1:
            return -1
        r = -1
        i = len(digits) - 1
        while i > p and r == -1:
            if digits[i] > digits[p]:
                r = i
                break
            i -= 1
        digits[p],digits[r] = digits[r],digits[p]
        tail = digits[p+1:]
        tail.reverse()
        res = self.to_int(digits[0:p+1] + tail)
        if res > max_n:
            return -1
        return res

sol = Solution()
print(sol.nextGreaterElement(1999999999))
print(sol.nextGreaterElement(230241))





