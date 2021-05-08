class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def flip(arr, k):
            i = 0
            j = k - 1
            while i <= j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1

        n = len(arr)
        res = []
        for i in range(n - 1, -1, -1):
            j = arr.index(i + 1)
            if i == j:
                continue
            # move item to 0 pos
            if j != 0:
                flip(arr, j + 1)
                res.append(j + 1)
            # move item to original pos
            flip(arr, i + 1)
            res.append(i + 1)
        return res