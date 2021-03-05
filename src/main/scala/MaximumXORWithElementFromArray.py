class Trie:
    def __init__(self):
        self.bin = {}

    def add(self, a):
        p = self.bin
        for i in range(31, -1, -1):
            d = (a >> i) & 1
            if d not in p:
                p[d] = {}
            p = p[d]

    def find(self, a):
        if not self.bin:
            return -1
        p = self.bin
        #get xored result
        res = 0
        for i in range(31, -1, -1):
            d = (a >> i) & 1
            if (1 - d) in p:
                # this is 1 because 1-d is opposite bit in x
                res |= (1 << i)
                p = p[1 - d]
            else:
                p = p[d]
        return res

class Solution:
    def maximizeXor(self, nums, queries):
        sorted_nums = sorted(nums)
        #sort nums
        sorted_indices = [i for i in range(len(queries))]
        #sort by second m
        sorted_indices = sorted(sorted_indices, key=lambda i: queries[i][1])
        last = 0
        trie = Trie()
        res = [-1] * len(queries)
        for i in sorted_indices:
            x,m = queries[i]
            #add number until sorted nums is <= m
            while last < len(sorted_nums) and sorted_nums[last] <= m:
                trie.add(sorted_nums[last])
                last += 1
            res[i] = trie.find(x)
        return res

sol = Solution()
print(sol.maximizeXor([0,1,2,3,4], [[3,1],[1,3],[5,6]]))#[3,3,7]
print(sol.maximizeXor([5,2,4,6,6,3],[[12,4],[8,1],[6,3]]))#[15,-1,5]




