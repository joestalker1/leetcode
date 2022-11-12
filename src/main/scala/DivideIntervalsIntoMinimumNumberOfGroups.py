class Solution:
    def minGroups(self, intervals) -> int:
        if not intervals:
            return 0
        events = []
        for s,e in intervals:
            events.append([s,1])
            events.append([e+1,-1])
        events.sort()
        max_cnt = 0
        cur_members_in_grp = 0
        for s,ev in events:
            cur_members_in_grp += ev
            max_cnt = max(max_cnt, cur_members_in_grp)
        return max_cnt