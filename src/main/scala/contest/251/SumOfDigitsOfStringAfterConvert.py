class Solution:
    def getLucky(self, s: str, k: int) -> int:
        nums = [ord(s[i]) - ord('a') +1 for i in range(len(s))]
        s = ''.join(list(map(str, nums)))
        num = sum(list(map(int, s)))

        for _ in range(k-1):
            s = 0
            while num:
                d = num % 10
                s += d
                num = num // 10
            num = s
        return num


sol = Solution()
print(sol.getLucky("leetcode",2))