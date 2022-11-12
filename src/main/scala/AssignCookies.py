class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # assert self._findContentChildren([], []) == 0,'test1'
        # assert self._findContentChildren([1],[1]) == 1,'test2'
        # assert self._findContentChildren([3,4],[1,2]) == 0,'test3'
        # assert self._findContentChildren([1,2,3],[1,1]) == 1,'test4'
        return self._findContentChildren(g, s)

    def _findContentChildren(self, g: List[int], s: List[int]) -> int:
        if not g or not s:
            return 0
        content_children = 0
        g.sort()
        s.sort()
        i = 0
        j = 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                i += 1
            j += 1
        return i


sol = Solution()
print(sol.findContentChildren([1,2], [1,2,3]))
print(sol.findContentChildren([1,2,3], [1,1]))


