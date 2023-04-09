from functools import lru_cache


class Solution:
    def possiblyEquals(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True

        @lru_cache(None)
        def dfs(i, j, diff):
            if i >= len(s1) and j >= len(s2) and diff == 0:
                return True
            if i < len(s1):
                if s1[i].isnumeric():
                    cnt = 0
                    val = 0
                    while i + cnt < len(s1) and cnt < 3 and s1[i + cnt].isnumeric():
                        val = 10 * val + int(s1[i + cnt])
                        cnt += 1
                        if dfs(i + cnt, j, diff - val):
                            return True
                else:
                    if diff > 0:
                        if dfs(i + 1, j, diff - 1):
                            return True
                    elif diff == 0 and j < len(s2) and s1[i] == s2[j]:
                        if dfs(i + 1, j + 1, diff):
                            return True
            if j < len(s2):
                if s2[j].isnumeric():
                    cnt = 0
                    val = 0
                    while j + cnt < len(s2) and cnt < 3 and s2[j + cnt].isnumeric():
                        val = 10 * val + int(s2[j + cnt])
                        cnt += 1
                        if dfs(i, j + cnt, diff + val):
                            return True
                elif diff < 0 and dfs(i, j + 1, diff + 1):
                    return True
            return False

        return dfs(0, 0, 0)