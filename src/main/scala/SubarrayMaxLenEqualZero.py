class Solution:
    def maxLen(self, n, arr):
        assert self._maxLen(1, [0]) == 1, '1 item array'
        assert self._maxLen(2, [1, -1]) == 2, '2 items array'
        assert self._maxLen(5, [1, 1, 2, -1, -1]) == 3, '5 items array'
        return self._maxLen(n, arr)

    def _maxLen(self, n, arr):
        seq_sum = {}
        cur_sum = 0
        max_len = 0
        for i in range(len(arr)):
            cur_sum += arr[i]
            if cur_sum == 0 and arr[i] == 0:
                max_len = 1
            if cur_sum == 0:
                max_len = i + 1
            if cur_sum in seq_sum:
                max_len = max(max_len, i - seq_sum[cur_sum])
            else:
                seq_sum[cur_sum] = i
        return max_len
