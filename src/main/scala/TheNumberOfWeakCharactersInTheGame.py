class Solution:
    def numberOfWeakCharacters(self, properties) -> int:
        if not properties:
            return 0
        #sort by attack in increasing order and sort by defense in decreasing order,
        #it gives that we don't count defense chars for the same attack
        properties.sort(key=lambda x:[x[0],-x[1]])
        weak = 0
        max_defense = 0
        #go from right to left
        for i in range(len(properties) - 1,-1,-1):
            if properties[i][1] < max_defense:
                weak += 1
            max_defense = max(max_defense, properties[i][1])
        return weak