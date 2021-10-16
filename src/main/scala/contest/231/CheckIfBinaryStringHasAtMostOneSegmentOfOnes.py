class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        cnt = 0
        last = None
        for i in range(len(s)):
            if last != s[i] and s[i] == '1':
                cnt += 1
            last = s[i]
        return cnt == 1

