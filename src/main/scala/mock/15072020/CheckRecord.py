class Solution:
    def checkRecord(self, s: str):
        if not s or len(s) == 0:
            return False

        countA = 0
        countL = 0
        for i in range(len(s)):
            if s[i] == 'A':
                countA += 1
                countL = 0
            elif s[i] == 'L':
                countL += 1
            else:
                countL = 0
            if countA > 1 or countL > 2:
                return False
        return True



