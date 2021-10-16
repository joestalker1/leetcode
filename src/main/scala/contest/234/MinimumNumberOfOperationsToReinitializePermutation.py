class Solution:
    def reinitializePermutation(self, n: int):

        def make_perm(arr, new_arr):
            for i in range(1, n-1):
                if i % 2 == 1:
                    new_arr[i] = arr[n//2 + (i-1) // 2]
                else:
                    new_arr[i] = arr[i//2]

        perm = [i for i in range(n)]
        arr = perm[::1]
        make_perm(perm, arr)
        arr, perm = perm, arr
        cnt = 1
        while perm[1] != 1:
            make_perm(perm, arr)
            arr,perm = perm,arr
            cnt += 1
        return cnt

sol = Solution()
print(sol.reinitializePermutation(8))
print(sol.reinitializePermutation(6))#4
print(sol.reinitializePermutation(4))#2
print(sol.reinitializePermutation(2))#1
