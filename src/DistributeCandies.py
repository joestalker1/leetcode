class Solution:
    def distributeCandies(self, candies):
        freq = {}
        sum = 0
        for i in range(len(candies)):
            candy = candies[i]
            if candy not in freq:
                freq[candy] = 1
                sum += 1
            else:
                freq[candy] = freq[candy] + 1
                sum += 1
        need = sum /2
        kinds = set()
        while need > 0:
            for k, v in freq.items():
                if v > 0 and need > 0:
                   kinds.add(k)
                   freq[k] = v - 1
                   need -= 1
                elif need == 0:
                    break

        return len(kinds)


sol = Solution()
print(sol.distributeCandies([1, 1, 2, 3]))
print(sol.distributeCandies([0, 0, 14, 0, 10, 0, 0, 0]))
