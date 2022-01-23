class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        # assert self._maxProfit([1],1) == 1, 'one ball'
        # assert self._maxProfit([1],2) == 1, 'one ball'
        # assert self._maxProfit([1,2],2) == 3, 'two balls'
        return self._maxProfit(inventory, orders)

    def _maxProfit(self, inventory: List[int], orders: int) -> int:
        MOD = 10 ** 9 + 7
        sorted_inv = [a for a in inventory]
        sorted_inv.sort()
        max_val = 0
        cnt = 1
        i = len(sorted_inv) - 1

        def calc_value(b, a):
            return (b - a) * (b + a + 1) // 2

        while orders:
            if i > 0 and (sorted_inv[i] - sorted_inv[i - 1]) > 0 and orders >= cnt * (
                    sorted_inv[i] - sorted_inv[i - 1]):
                orders -= cnt * (sorted_inv[i] - sorted_inv[i - 1])
                max_val += cnt * calc_value(sorted_inv[i], sorted_inv[i - 1])
            elif i == 0 or (sorted_inv[i] - sorted_inv[i - 1]) > 0:
                can_sell = orders // cnt
                rem = orders % cnt
                max_val += cnt * calc_value(sorted_inv[i], sorted_inv[i] - can_sell)
                max_val += (sorted_inv[i] - can_sell) * rem
                orders = 0
            i -= 1
            cnt += 1
            max_val %= MOD
        return max_val
