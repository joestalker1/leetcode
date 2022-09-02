from math import inf

class Solution:
    def shortestSequence(self, rolls, k: int) -> int:

        def find_all_seq(i, cur_len):
            if cur_len == len(rolls):
                return inf
            min_seq_len = inf
            for s in range(1, k + 1):
                cand = None
                for j in range(i, len(rolls)):
                    if s == rolls[j]:
                        cand = s
                        break
                if not cand:
                    return cur_len-1
                min_seq_len = min(find_all_seq(i + 1, cur_len + 1), min_seq_len)
            return min_seq_len

        min_seq_len = find_all_seq(0, 1)
        return min_seq_len


sol = Solution()
print(sol.shortestSequence([4,2,1,2,3,3,2,4,1], 4))#3
print(sol.shortestSequence([1,1,2,2], 2))#2
