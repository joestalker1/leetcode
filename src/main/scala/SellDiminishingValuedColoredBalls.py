class Solution:
    def maxProfit(self, inventory, orders: int) -> int:
        # assert self._maxProfit([1],1) == 1, 'one ball'
        # assert self._maxProfit([1],2) == 1, 'one ball'
        # assert self._maxProfit([1,2],2) == 3, 'two balls'
        return self._maxProfit(inventory, orders)

    def _maxProfit(self, inventory, orders: int) -> int:
        MOD = 10 ** 9 + 7
        sorted_inv = [a for a in inventory]
        sorted_inv.sort()
        max_val = 0
        width = 1
        i = len(sorted_inv) - 1

        def sum_from_b_to_a(b, a):
            return b * (b + 1) // 2 - a * (a + 1) // 2

        while orders:
            if i > 0 and (sorted_inv[i] - sorted_inv[i - 1]) > 0 and orders >= width * (
                    sorted_inv[i] - sorted_inv[i - 1]):
                # subtract ball number
                orders -= width * (sorted_inv[i] - sorted_inv[i - 1])
                # count score from selling balls
                max_val += width * sum_from_b_to_a(sorted_inv[i], sorted_inv[i - 1])
            elif i == 0 or (sorted_inv[i] - sorted_inv[i - 1]) > 0:
                # how many rows we need
                rows = orders // width
                rem = orders % width
                max_val += width * sum_from_b_to_a(sorted_inv[i], sorted_inv[i] - rows)
                max_val += (sorted_inv[i] - rows) * rem
                orders = 0
            i -= 1
            width += 1
            max_val %= MOD
        return max_val
