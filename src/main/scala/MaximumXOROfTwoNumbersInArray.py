class Trie:
    def __init__(self):
        self.bin = {}

    def add(self, a):
        p = self.bin
        for i in range(31,-1,-1):
            d = (a >> i) & 1
            if d not in p:
                p[d] = {}
            p = p[d]

    def find(self, a):
        if not self.bin:
            return -1
        p = self.bin
        res = 0
        for i in range(31, -1, -1):
            d = (a >> i) & 1
            if (1 - d) in p:
                res |= (1 << i)
                p = p[1 - d]
            else:
                p = p[d]
        return res


class Solution:
    def findMaximumXOR(self, nums):
        max_xor = 0
        trie = Trie()
        trie.add(nums[-1])
        for i in range(len(nums)-1,-1,-1):
            xor = trie.find(nums[i])
            max_xor = max(xor, max_xor)
            trie.add(nums[i])
        return max_xor


sol = Solution()
print(sol.findMaximumXOR([3,10,5,25,2,8]))
