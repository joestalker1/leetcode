class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        if n == 1 and k == 1:
            return '0'
        s = '0' * (n - 1)

        res = []
        seen = set()

        def dfs(cur, seen):
            # for every edge with x
            for x in range(k):
                # go by edge
                # new node
                nei = cur + str(x)
                # if we visit it, let's skip it.
                if nei not in seen:
                    # go from the next vertex
                    seen.add(nei)
                    dfs(nei[1:], seen)
                    res.append(str(x))

        dfs(s, seen)
        return ''.join(res) + s


sol = Solution()
print(sol.crackSafe(2, 2))#"00110"
print(sol.crackSafe(1, 2))