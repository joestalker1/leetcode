class Solution:
    def minOperations(self, s):
        res1 = 0
        # zero is at odd position
        for i in range(len(s)):
            if i % 2 == 0:
                if s[i] != '1':
                    res1 += 1
            else:
                if s[i] != '0':
                    res1 += 1
        res2 = 0
        # zero is at even position
        for i in range(len(s)):
            if i % 2 == 0:
                if s[i] != '0':
                    res2 += 1
            else:
                if s[i] != '1':
                    res2 += 1
        return min(res1, res2)
