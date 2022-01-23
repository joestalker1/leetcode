from functools import lru_cache

class Solution:
    def mostPoints(self, questions) -> int:

        @lru_cache(None)
        def solve(cur_quest):
            if cur_quest >= len(questions):
                return 0
            # if cur_quest in mem:
            #     return mem[cur_quest]
            # take or skip it
            return max(questions[cur_quest][0] + solve(cur_quest + questions[cur_quest][1]+1), solve(cur_quest + 1))

        return solve(0)


sol = Solution()
print(sol.mostPoints([[21,2],[1,2],[12,5],[7,2],[35,3],[32,2],[80,2],[91,5],[92,3],[27,3],[19,1],[37,3],[85,2],[33,4],[25,1],[91,4],[44,3],[93,3],[65,4],[82,3],[85,5],[81,3],[29,2],[25,1],[74,2],[58,1],[85,1],[84,2],[27,2],[47,5],[48,4],[3,2],[44,3],[60,5],[19,2],[9,4],[29,5],[15,3],[1,3],[60,2],[63,3],[79,3],[19,1],[7,1],[35,1],[55,4],[1,4],[41,1],[58,5]]))
print(sol.mostPoints([[3,2],[4,3],[4,4]]))#4
print(sol.mostPoints([[1,1],[2,2],[3,3],[4,4],[5,5]]))#7
