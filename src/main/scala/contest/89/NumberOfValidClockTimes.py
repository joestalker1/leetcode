class Solution:
    def countTime(self, time: str) -> int:
        if not time:
            return 0
        cnt1 = 1
        if time[0] == '?':
            cnt1 = 3
            if time[1] > '3':
                cnt1 -= 1
        #1,2,3,4,5,6,7,9,0 if h = 0,1 - 0,1,2,3 if h = 2
        if time[1] == '?':
            if time[0] == '?':
                cnt1 = 24
            elif time[0] == '2':
                cnt1 = 4
            elif time[0] == '0':
                cnt1 = 10
            elif time[0] == '1':
                cnt1 = 10
            else:
                cnt1 = 10
        cnt2 = 1
        if time[3] == '?':
            cnt2 = 6
        if time[4] == '?':
            if time[3] == '?':
                cnt2 = 60
            elif time[3] in ['0','1','2','3','4','5']:
                cnt2 = 10
            else:
                cnt2 = 10
        return cnt1 * cnt2


sol = Solution()
print(sol.countTime("1?:?6"))#60
print(sol.countTime('0?:0?'))