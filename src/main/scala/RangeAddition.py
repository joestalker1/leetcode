class Solution:
    def getModifiedArray(self, length: int, updates):
        arr = [0] * length
        for s,e,x in updates:
            arr[s] += x
            if e < length - 1:
                arr[e + 1] -= x
        for i in range(1, length):
            arr[i] += arr[i-1]
        return arr