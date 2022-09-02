class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        #n & (n -1) == 0 if n is power of 2 and n is power of 4
        return n > 0 and n &(n-1) == 0 and n & 0xaaaaaaaa == 0