class Solution:
    def decode(self, encoded):
        n = len(encoded) + 1
        xor = 0
        for i in range(1, n + 1):
            xor = xor ^ i
        perm = [0] * n
        perm[-1] = xor
        # calculate last perm using odd encoded[0],encoded[2] and so on.
        for i in range(0 ,len(encoded), 2):
            perm[-1] ^= encoded[i]
        # calculate the rest of perm
        for i in range(len(encoded) - 1, -1, -1):
            perm[i] = perm[i + 1] ^ encoded[i]
        return perm
