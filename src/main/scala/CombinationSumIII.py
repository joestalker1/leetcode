class Solution:
    def combinationSum3(self, k: int, n: int):
        self._combinationSum3(3, 3) == [[1, 1, 1]], 'test1'
        self._combinationSum3(2, 4) == [[1, 3], [2, 2]], 'test2'
        return self._combinationSum3(k, n)

    def _combinationSum3(self, k: int, n: int):
        if k == 0 or n == 0:
            return []

        def gen_comb(start, cur_sum, buf, res):
            if cur_sum > n:
                return
            if len(buf) == k:
                if cur_sum == n:
                    res.append(buf)
                return
            for b in range(start, 10):
                if cur_sum + b > n:
                    return
                gen_comb(b + 1, cur_sum + b, buf + [b], res)

        res = []
        gen_comb(1, 0, [], res)
        return res


