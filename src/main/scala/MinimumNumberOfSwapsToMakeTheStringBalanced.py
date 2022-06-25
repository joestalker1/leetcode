class Solution:
    def minSwaps(self, s: str) -> int:
        if not s:
            return 0
        opened = 0
        swaps = 0
        for i in range(len(s)):
            if s[i] == '[':
                opened += 1
            else:
                if i+1 > 2*opened:
                    opened += 1
                    swaps += 1
        return swaps


sol = Solution()
#print(sol.minSwaps("[]"))#0
print(sol.minSwaps("]["))#1
print(sol.minSwaps("][[]][][[][]"))#1