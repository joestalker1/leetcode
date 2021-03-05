class Solution:
    def numberOfMatches(self, n: int):

        def count_matches(n):
            if n <= 1:
                return 0
            if n % 2 == 0:
                return n// 2 + count_matches(n // 2)
            return (n-1)//2 + count_matches(1 + (n - 1) // 2)
        return count_matches(n)

