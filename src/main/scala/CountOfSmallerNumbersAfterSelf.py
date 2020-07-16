class Solution:
    def countSmaller(self, nums):
        if not nums or len(nums) == 0:
            return nums
        counts = [0] * len(nums)
        arr = [(a,i) for i,a in enumerate(nums)]

        def merge_sort(arr, counts):
            if len(arr) > 1:
                mid = len(arr) // 2
                L = arr[:mid]
                R = arr[mid:]
                merge_sort(L, counts)
                merge_sort(R, counts)
                i = j = k = 0
                moves = 0
                while i < len(L) and j < len(R):
                    if L[i][0] > R[j][0]:
                        arr[k] = R[j]
                        moves += 1
                        k += 1
                        j += 1
                    else:
                        arr[k] = L[i]
                        counts[L[i][1]] += moves
                        i += 1
                        k += 1

                while i < len(L):
                    counts[L[i][1]] += moves
                    arr[k] = L[i]
                    i += 1
                    k += 1

                while j < len(R):
                    arr[k] = R[j]
                    j += 1
                    k += 1

        merge_sort(arr, counts)
        return counts



sol = Solution()
print(sol.countSmaller([5,2,6,1]))
print(sol.countSmaller([7, 6, 1, 1]))
print(sol.countSmaller([2, 0, 1]))
