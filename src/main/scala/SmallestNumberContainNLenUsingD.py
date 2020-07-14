class Solution:
    def smallestNumber(self, N, D):
        ans = []
        visited = set()
        start = ['0'] * (N - 1)

        def dfs(S, D, visited):
            nonlocal ans
            for i in range(0, D):
                S.append(str(i))
                s = ''.join(S)
                if s not in visited:
                    visited.add(s)
                    dfs(S[1:], D, visited)
                    ans.append(str(i))
                S.pop(-1)

        dfs(start, D, visited)
        ans.append(''.join(start))
        return ''.join(ans)


sol = Solution()
print(sol.smallestNumber(2,2))



