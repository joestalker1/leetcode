class Solution:
    def xorQueries(self, arr, queries):
        prefix = [0] * len(arr)
        prefix[0] = arr[0]
        #make prefix of xored values
        for i in range(1, len(arr)):
            prefix[i] = prefix[i-1] ^ arr[i]
        res = []
        # values from 0 to l will be zero.
        for l,r in queries:
            if l == 0:
                res.append(prefix[r])
            else:
                res.append(prefix[r] ^ prefix[l - 1])
        return res
