class Solution:
    def ipToInt(self, x):
        ans = 0
        for a in x.split('.'):
            ans = ans << 8
            ans += int(a)
        return ans

    def intToIp(self, a):
        return '.'.join(str((a >> i) % 256) for i in (24, 16, 8, 0))

    def ipToCIDR(self, ip, n):
        start = self.ipToInt(ip)
        ans = []
        while n:
            n1 = start.bit_length()
            n2 = n.bit_length()
            mask = max(33 - (start & -start).bit_length(),
                       33 - n.bit_length())
            ans.append(self.intToIp(start) + '/' + str(mask))
            start += 1 << (32 - mask)
            n -= 1 << (32 - mask)
        return ans

sol = Solution()
print(sol.ipToCIDR("117.145.102.62", 8))
print(sol.ipToCIDR("255.0.0.7", 10))