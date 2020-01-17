class Solution:
    def array_two_elements(self, arr):
        if not arr:
            return []
        xor = 0
        for a in arr:
            xor = xor ^ a
        # get rigtmost bit
        xor = xor & -xor
        rets = [0, 0]

        for a in arr:
            # look up the num with this bit is 1
            if a & xor:
                rets[0] = rets[0] ^ a
            else:
                rets[1] = rets[1] ^ a
        return rets

sol = Solution()
print(sol.array_two_elements([2, 4, 6, 8, 10, 2, 6, 10]))
