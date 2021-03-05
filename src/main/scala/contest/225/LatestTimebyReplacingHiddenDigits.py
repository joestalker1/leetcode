class Solution:
    def maximumTime(self, time):
        rules = {0: '2', 1: '3', 3: '5', 4: '9'}
        s = list(time)
        i = 0
        while i < len(s):
            if s[i] == ':':
                i += 1
                continue
            if i == 0 and s[i] == '?' and s[i + 1] == '?':
                s[i] = '2'
                s[i + 1] = '3'
                i += 2
                continue
            elif i == 3 and s[i] == '?' and s[i+1] == '?':
                s[i] = '5'
                s[i+1] = '9'
                i += 2
                continue
            elif i == 0 and s[i] == '?':
                a = int(s[i + 1])
                if a < 4:
                    s[i] = '2'
                else:
                    s[i] = '1'
            elif i == 1 and (s[i - 1] == '0' or s[i - 1] == '1') and s[i] == '?':
                s[i] = '9'
            elif s[i] == '?':
                s[i] = rules[i]
            i += 1
        return ''.join(s)

sol = Solution()
print(sol.maximumTime("1?:??"))
print(sol.maximumTime("??:??"))
print(sol.maximumTime("??:?5"))#23:55
