def quick_sort(arr, i, j):
    if i < j:
        pivot = arr[i]
        k = i
        i += 1
        l = k + 1
        while l <= j:
            if arr[l] >= pivot:
                arr[i], arr[l] = arr[l], arr[i]
                i += 1
            l += 1
        t = arr[i - 1]
        arr[i - 1] = pivot
        arr[k] = t
        quick_sort(arr, k, i - 2)
        quick_sort(arr, i, j)

class Solution:
    def findContentChildren(self, g, s):
        if not g or not s:
            return 0
        quick_sort(g, 0, len(g) - 1)
        quick_sort(s, 0, len(s) -1)
        last_cookie = -1
        res = 0
        for greed in g:
            j = last_cookie + 1
            if 0 <= j < len(s) and greed <= s[j]:
                last_cookie = j
                res += 1
        return res


sol = Solution()
print(sol.findContentChildren([1,2], [1,2,3]))
print(sol.findContentChildren([1,2,3], [1,1]))


