class TrieNode:
    def __init__(self, bitsPerNum=16):
        self.table = [None,None]
        self.cnt = 0

class Solution:
    def insertTrie(self, node, n, bitsPerNum=16):
        for i in range(bitsPerNum,-1,-1):
            x = (n >> i) & 1
            if not node.table[x]:
                node.table[x] = TrieNode()
            node.table[x].cnt += 1
            node = node.table[x]

    def countSmallerPair(self, node, n, limit,bitsPerNum=16):
        i = bitsPerNum
        cnt = 0
        for i in range(bitsPerNum,-1,-1):
            if not node:
                break
            x = (n >> i) & 1
            y = (limit >> i) & 1
            if y == 0:
                #consider next bit, current bits don't matter
                node = node.table[x]
                continue
            #y is 1
            if node.table[x]:
                #if trie bit is as x so it gives 0 and it's less 1
                cnt += node.table[x].cnt
            # go on with another bit
            node = node.table[1 - x]
        return cnt

    def countPairs(self, nums, low: int, high: int) -> int:
        if not nums or len(nums) < 2:
            return 0
        trie = TrieNode()
        cnt = 0
        bitsPerNum = 16
        for i in range(len(nums)):
            cnt += self.countSmallerPair(trie, nums[i], high + 1, bitsPerNum) - self.countSmallerPair(trie, nums[i], low, bitsPerNum)
            self.insertTrie(trie, nums[i], bitsPerNum)
        return cnt


sol = Solution()
print(sol.countPairs([1,4,2,7], 2, 6))#6
