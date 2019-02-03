import re

class Solution:
    def is_valid_ip4_group(self, a):
        i = 0
        while i < len(a) and a[i] == '0':
            i += 1
        b = int(a[i:])
        return 0 <= b <= 255

    def check_ip4(self, ip):
        res = re.match(r'^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$', ip)
        if not res:
            return "Neither"
        for i in range(1, 5):
            if not self.is_valid_ip4_group(res[i]):
                return "Neither"
        return "IPv4"

    def check_ip6(self, ip):
        res = re.search('^([0-9abcdefABCDEF]{1,4}):([0-9abcdefABCDEF]{1,4}):([0-9abcdefABCDEF]{1,4}):([0-9abcdefABCDEF]{1,4}):([0-9abcdefABCDEF]{1,4}):([0-9abcdefABCDEF]{1,4}):([0-9abcdefABCDEF]{1,4}):([0-9abcdefABCDEF]{1,4})$', ip)
        if not res:
            return "Neither"
        return "IPv6"


    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        if not IP:
            return "Neither"
        if "." in IP:
            return self.check_ip4(IP)
        return self.check_ip6(IP)


sol = Solution()
print(sol.validIPAddress("01.01.01.01"))
print(sol.validIPAddress("2001:0db8:85a3:0:0:8A2E:0370:7334"))
print(sol.validIPAddress("172.16.254.1"))