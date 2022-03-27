class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        #reserve 'a' for all positions
        k -= n
        num = [0] * n
        for i in range(n-1, -1, -1):
            #assign 26-1 = 25 if it's min o
            add = min(25, k)
            num[i] = chr(ord('a') + add)
            k -= add
        return ''.join(num)
