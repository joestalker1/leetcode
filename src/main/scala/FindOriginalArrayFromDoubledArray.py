class Solution:
    def findOriginalArray(self, changed):
        # assert self._findOriginalArray([1,2,3]) == [],'test1'
        # assert self._findOriginalArray([]) == [], 'test2'
        # assert self._findOriginalArray([2,1,6,3]) == [1,3], 'test3'
        return self._findOriginalArray(changed)

    def _findOriginalArray(self, changed):
        if not changed or len(changed) % 2 == 1:
            return []
        original = []
        max_val = max(changed)
        freq = [0] * (2 * max_val + 1)
        for num in changed:
            freq[num] += 1
        num = 0
        # if freq[num] > 1,it run loop for every num
        while num <= max_val:
            if freq[num] == 0:
                num += 1
                continue
            # decrement
            freq[num] -= 1
            twice_val = num * 2
            if freq[twice_val] == 0:
                return []
            original.append(num)
            freq[twice_val] -= 1
        return original