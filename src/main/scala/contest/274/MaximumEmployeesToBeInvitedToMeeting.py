from functools import lru_cache
class Solution:
    def maximumInvitations(self, favorite) -> int:
        if not favorite:
            return 0
        n = len(favorite)
        max_emp_num = 0

        #@lru_cache(None)
        def count_grp(v, seen):
            if ((1 << v) & seen) != 0:
                cnt = 0
                for i in range(n):
                    if ((1 << i) & seen) != 0:
                        cnt += 1
                return cnt
            return count_grp(favorite[v], seen | (1 << v))

        for i in range(n):
            cur_cnt = count_grp(i, 0)
            max_emp_num = max(max_emp_num, cur_cnt)
        return max_emp_num



sol = Solution()
print(sol.maximumInvitations([3,0,1,4,1]))#4
print(sol.maximumInvitations([2,2,1,2]))#3