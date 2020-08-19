class Solution:
    def partition(self, s: str):
        if not s:
            return s

        def is_poly(sub, l,h):
            if l == h:
                return True
            while l < h:
                if sub[l] != sub[h]:
                    return False
                l += 1
                h -= 1
            return True

        def backtrack(arr, res, temp, start):
            if start == len(s):
                res.append(temp[::])
                return
            for k in range(start, len(arr)):
                if is_poly(arr, start, k):
                    temp.append(arr[start, k+1])
                    backtrack(arr, res, temp, k + 1)
                    temp.pop(-1)

        res = []
        backtrack(list(s), res, [], 0)
        return res

