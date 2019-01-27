class Solution:
    def decode(self, mem, s, i):
        if i == len(s):
            return 1
        kk = s[i:]
        if kk in mem.keys():
            return mem[kk]
        w = 0
        if i + 1 <= len(s):
            if self.str_to_num(s, i, 1) >= 1:
                w += self.decode(mem, s, i + 1)

        if i + 2 <= len(s) and s[i] != '0':
            if self.str_to_num(s, i, 2) <= 26:
                w += self.decode(mem, s, i + 2)
        mem[kk] = w
        return w

    def str_to_num(self, s, i, count):
        num = 0
        base = 1
        for i in range(i + count - 1, i - 1, -1):
            num += (ord(s[i]) - ord('0')) * base
            base *= 10
        return num

    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s.find("00") != -1 or s[0] == '0':
            return 0
        return self.decode({}, s, 0)


sol = Solution()
print(sol.numDecodings(
    "9371597631128776948387197132267188677349946742344217846154932859125134924241649584251978418763151253"))
print(sol.numDecodings("01"))
print(sol.numDecodings("1001"))
print(sol.numDecodings("27"))
print(sol.numDecodings("226"))
print(sol.numDecodings("12"))
