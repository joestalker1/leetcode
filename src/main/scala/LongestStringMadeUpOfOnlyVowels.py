class Solution:
    def solution(self, S):
        if not S:
            return 0
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        start = 0
        while start < len(S) and S[start] in vowels:
            start += 1
        end = len(S) - 1
        while end >= 0 and S[end] in vowels:
            end -= 1
        if start >= len(S):
            return 0
        res = start + len(S) - end - 1
        count = 0
        longest = 0
        for i in range(start, end + 1):
            if S[i] in vowels:
                count += 1
            else:
                count = 0
            longest = max(count, longest)
        return res + longest


sol = Solution()
print(sol.solution('earthproblem'))