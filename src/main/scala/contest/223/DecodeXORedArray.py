class Solution:
    def decode(self, encoded, first):
        arr = []
        arr.append(first)

        def find_b(a, r):
            b = 0
            for i in range(31, -1, -1):
                b1 = a & (1 << i)
                b2 = r & (1 << i)
                if b1 != b2:
                    b |= (1 << i)
            return b

        for i in range(len(encoded)):
            arr.append(find_b(arr[-1], encoded[i]))
        return arr


sol = Solution()
print(sol.decode([1, 2, 3], 1))
