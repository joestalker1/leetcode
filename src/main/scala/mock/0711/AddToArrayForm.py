class Solution:
    def addToArrayForm(self, A, K):
        if not A or K == 0:
            return A
        f = []
        a = K
        while a:
            r = a % 10
            f.insert(0, r)
            a = a // 10
        res = []
        carry = 0
        for i in range(min(len(f, A))):
            a1 = A[-(i + 1)]
            a2 = f[-(i + 1)]
            a = a1 + a2 + carry
            r = a % 10
            res.insert(0, r)
            carry = a // 10
        if len(A) != len(f):
            arr = A
            n = len(A)
            if len(A) < len(f):
                arr = f
                n = len(f)
            for j in range(i, n):
                a1 = arr[-(j+1)]
                a1 += carry
                carry = a1 // 10
                res.insert(0, a1)
        if carry:
            res.insert(0, carry)
        return res




