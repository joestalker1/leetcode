class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        # 4 -> 2,1,,
        # need to roll from 1 to k at every position
        # @ 1,1,2,2 can form 1 length 1,2 ; 1,1, 2,1 2,2

        cur_len = 1
        all_num = set()
        for i in range(len(rolls)):
            all_num.add(rolls[i])
            if len(all_num) == k:
                cur_len += 1
                all_num = set()
        return cur_len
