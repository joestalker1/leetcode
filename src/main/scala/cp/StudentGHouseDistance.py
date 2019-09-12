class Solution:
    def matching(self, bit_mask, memo, n):
        dist = [0] * 20
        for i,row in enumerate(dist):
            row[i] =  

        if memo[bit_mask] > -0.5:
            return memo[bit_mask]
        if bit_mask == (1 << 2 * n) - 1:
            memo[bit_mask] = 0
            return memo[bit_mask]
        matching_value = 32767 ** 2

        for p1 in range(2 * n):
            for p2 in range(p1 + 1, 2*n):
                if not (bit_mask > 0 and (1 << p2) > 0):
                    matching_value = min(matching_value, )





