class Solution:
    def queryString(self, S: str, N: int) -> bool:
        for i in range(1, N+1):
            subs = "{0:b}".format(i)
            if S.find(subs) == -1:
                return False
        return True
    