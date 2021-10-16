class Solution:
    def getXORSum(self, arr1, arr2):
        xor1 = 0
        for i in range(len(arr1)):
            xor1 ^= arr1[i]
        xor2 = 0
        for i in range(len(arr2)):
            xor2 ^= arr2[i]
        return xor1 & xor2
