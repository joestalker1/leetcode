class Solution:
    def atoi(self, a):
        return int(a)

    def itoa(self, a):
        return repr(a)

    def handle_two_chars(self, ch1, ch2, m, sum_of_two, carry = ''):
        prd = m[ch1 + ch2]
        res = ''
        if len(prd) > 1:
            ch = prd[1]
        else:
            ch = prd[0]
        if carry != '':
            ch = self.sum(sum_of_two, carry, ch)
            if len(ch) > 1:
                carry = ch[0]
                ch = ch[1]
                res = ch + res
                return (res, carry)
        res = ch + res
        if len(prd) > 1:
            carry = prd[0]
        else:
            carry = ''
        return (res, carry)

    def sum(self, sum_of_two, s1, s2):
        i = len(s1) - 1
        j = len(s2) - 1
        carry = ''
        res = ''
        while i >= 0 and j >= 0:
            (ch, carry) = self.handle_two_chars(s1[i], s2[j], sum_of_two, sum_of_two, carry)
            res = ch + res
            i -= 1
            j -= 1
        if i >= 0:
            if len(carry) > 0:
                a = self.sum(sum_of_two, s1[0:i+1], carry)
            else:
                a = s1[0:i + 1]
            res = a + res
        elif j >= 0:
            if len(carry) > 0:
                a = self.sum(sum_of_two, s2[0:j + 1], carry)
            else:
                a = s2[0:j+1]
            res = a + res
        elif len(carry) > 0:
            res = carry + res
        return res


    def multiply(self, num1, num2):
        if not num1 or not num2:
            return ''
        sum_of_two = {}
        prod = {}
        for a in range(10):
            for b in range(10):
                c = self.itoa(a + b)
                sum_of_two[repr(a) + repr(b)] = c
                d = self.itoa(a * b)
                prod[repr(a) + repr(b)] = d

        if len(num1) < len(num2):
            num1, num2 = num2, num1
        nums = []
        for k in range(len(num2)):
            res = ''
            s = num2[k]
            i = len(num1) - 1
            carry = ''
            while i >= 0:
                (ch, carry) = self.handle_two_chars(num1[i], s, prod, sum_of_two, carry)
                res = ch + res
                i -= 1
            if len(carry) > 0:
                a = self.sum(sum_of_two, num1[0:i + 1], carry)
            else:
                a = num1[0:i+1]
            res = a + res
            res += ('0' * (len(num2) - k - 1))
            nums.append(res)
        a = nums[0]
        for i in range(1, len(nums)):
            a = self.sum(sum_of_two, a, nums[i])
        # if all chars is zero let's convert it to one char
        if len(list(filter(lambda x: x == '0', a))) == len(a):
            a = '0'
        return a

sol = Solution()
print(sol.multiply("9133", "0"))
print(sol.multiply("999", "999"))
#print(sol.multiply("123","456"))







