from collections import defaultdict

class Solution:
    def numEquivDominoPairs(self, dominoes):
        if not dominoes:
            return 0
        mem = defaultdict(lambda: [0] * 10)
        pairs = 0
        for i in range(len(dominoes)):
            c, d = dominoes[i]
            arr = mem[c]
            pairs += arr[d]
            if c != d:
                arr = mem[d]
                pairs += arr[c]

            mem[c][d] += 1
        return pairs



sol = Solution()
print(sol.numEquivDominoPairs([[1,1],[2,2],[1,1],[1,2],[1,2],[1,1]]))#4
print(sol.numEquivDominoPairs([[1, 2], [1, 2], [1, 2]]))  # 3
print(sol.numEquivDominoPairs([[1, 2], [2, 1], [3, 4], [5, 6]]))
