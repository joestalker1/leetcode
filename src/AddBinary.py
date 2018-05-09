class Solution(object):
    def addBinary(self, a, b):
        if len(a) > len(b):
            s1 = a
            s2 = b
        else:
            s1 = b
            s2 = a
        shift = 0
        res = ""
        for i in range(len(s2) - 1, -1, -1):
            a = s2[i]
            a = ord(a) - ord('0')
            b = s1[i]
            b = ord(b) - ord('0')
            c = a + b
            c += shift
            if c >= 2:
               shift = c // 2
               c = c % 2
            else:
               shift = 0
            c += ord('0')
            res = chr(c) + res
        len_of_left_part = len(s1) - len(s2)
        for i in range(len_of_left_part - 1, -1, -1):
            a = ord(s1[i]) - ord('0')
            a += shift
            if a >= 2:
               shift = a // 2
               a = a % 2
            else:
               shift = 0
            a += ord('0')
            res = chr(a) + res
        if shift:
            c = ord('0') + shift
            res = chr(c) + res
        return res


sol = Solution()
#"110110"
print(sol.addBinary("100", "110010"))



        res = ""
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        while i >= 0 or j >= 0:
            sum = carry
            if i >= 0:
                sum += ord(a[i]) - ord('0')
                i -= 1
            if j >= 0:
                sum += ord(b[j]) - ord('0')
                j -= 1
            res += chr((sum % 2) + ord('0'))
            carry = sum // 2
        if carry:
            res += chr(carry + ord('0'))
        return res[::-1]


sol = Solution()
print(sol.addBinary("11", "1"))
print(sol.addBinary("100", "110010"))
