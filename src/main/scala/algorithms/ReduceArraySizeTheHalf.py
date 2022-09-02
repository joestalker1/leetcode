import math,collections

class Solution:
    def minSetSize(self, arr) -> int:
        # In Python, we can use the built-in Counter class.
        counts = collections.Counter(arr)
        max_val = max(counts.values())
        buckets = [0] * (max_val + 1)
        for cnt in counts.values():
            buckets[cnt] += 1

        set_size = 0
        arr_num_to_remove = len(arr) // 2
        bucket = max_val
        while arr_num_to_remove > 0:
            need_from_bucket = min(buckets[bucket], math.ceil(arr_num_to_remove / bucket))
            set_size += need_from_bucket
            arr_num_to_remove -= bucket * need_from_bucket
            bucket -= 1
        return set_size