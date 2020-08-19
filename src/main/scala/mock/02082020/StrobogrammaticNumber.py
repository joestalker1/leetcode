from collections import Counter


class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        if not num:
            return False
        i = 0
        j = len(num) - 1
        allowed = set(['0', '1', '8', '6', '9'])
        while i < j:
            a = num[i]
            b = num[j]
            if a not in allowed or b not in allowed:
                return False
            if a == b and a in ['0', '1', '8'] or a == '6' and b == '9' or a == '9' and b == '6':
                i += 1
                j -= 1
                continue
            else:
                return False

        return num[i] in ['0', '1', '8'] if len(num) == 1 else True

