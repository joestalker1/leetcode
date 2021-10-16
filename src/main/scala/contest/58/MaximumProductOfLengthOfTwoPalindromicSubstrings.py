class Solution:
    def maxProduct(self, s):
        def manachers(S):
            A = '@#' + '#'.join(S) + '#$'
            Z = [0] * len(A)
            center = 0
            right = 0
            for i in range(1, len(A) - 1):
                if i < right:
                    Z[i] = min(right - i, Z[2 * center - i])
                while A[i + Z[i] + 1] == A[i - Z[i] - 1]:
                    Z[i] += 1
                if i + Z[i] > right:
                    center = i
                    right = i + Z[i]
            return Z[2:-2:2]

        def helper(s):
            man = manachers(s)
            n = len(s)
            intervals = [(i - man[i] // 2, i + man[i] // 2) for i in range(n)]
            arr = [0] * n
            for a, b in intervals:
                arr[b] = max(arr[b], b - a + 1)
            for i in range(n - 2, -1, -1):
                arr[i] = max(arr[i], arr[i + 1] - 2)
            max_int = [0] * len(arr)
            max_int[0] = arr[0]
            for i in range(1, len(arr)):
                max_int[i] = max(max_int[i - 1], arr[i])
            return max_int
        t1 = helper(s)
        t2 = helper(s[::-1])[::-1]
        t2 = t2[1:] + [0]
        max_prod = 0
        for i in range(len(t1)):
            max_prod = max(max_prod, t1[i]*t2[i])
        return max_prod

sol = Solution()
print(sol.maxProduct("ggbswiymmlevedhkbdhntnhdbkhdevelmmyiwsbgg"))#45
print(sol.maxProduct("zaaaxbbby"))#9
print(sol.maxProduct("ababbb"))#9