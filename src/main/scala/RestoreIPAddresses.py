class Solution:
    def restoreIpAddresses(self, s):
        if not s:
            return s

        def generate_ip(part, i, ip, res):
            if part == 4:
                ip_len = len(ip[0]) + len(ip[1]) + len(ip[2]) + len(ip[3])
                if ip_len >= len(s):
                    ip_str = '.'.join(ip)
                    if len(res) > 0:
                        if res[-1] != ip_str:
                            res.append(ip_str)
                    else:
                        res.append(ip_str)
                return
            for j in range(1, 4):
                if (i + j) > len(s):
                    break
                a = int(s[i: i + j])
                if a <= 255:
                    ip[part] = repr(a)
                    generate_ip(part + 1, i + j, ip, res)
        res = []
        ip = [0] * 4
        generate_ip(0, 0, ip, res)
        return res



sol = Solution()
print(sol.restoreIpAddresses("010010"))
print(sol.restoreIpAddresses("25525511135"))