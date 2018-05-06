class Solution:
    def numJewelsInStones(self, J, S):
        jew = set(list(J))
        count = 0
        for stone in list(S):
            if stone in jew:
                count+= 1
        return count

sol = Solution()
print(sol.numJewelsInStones("aA", "aAAbbbb"))

