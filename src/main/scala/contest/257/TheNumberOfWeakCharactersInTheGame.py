class Solution:
    def numberOfWeakCharacters(self, properties) -> int:
        if not properties:
            return 0

        properties.sort(key=lambda x: [x[0], -x[1]])
        weak = 0
        max_defense = 0
        for i in range(len(properties) - 1, -1, -1):
            if properties[i][1] < max_defense:
                weak += 1
            max_defense = max(max_defense, properties[i][1])
        return weak


sol = Solution()
print(sol.numberOfWeakCharacters([[5,5],[6,3],[3,6]]))#0
print(sol.numberOfWeakCharacters([[7,7],[1,2],[9,7],[7,3],[3,10],[9,8],[8,10],[4,3],[1,5],[1,5]]))#6
print(sol.numberOfWeakCharacters([[1,5],[10,4],[4,3]]))#1