class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        n = len(s1)
        x1 = 0
        y1 = 0
        x2 = 0
        y2 = 0
        for i in range(n):
            if s1[i] == s2[i]:
                continue
            if s1[i] == 'x':
                x1+=1
            else:
                y1+=1
            if s2[i] == 'x':
                x2 += 1
            else:
                y2 += 1
        # if number of x or y is odd, return -1
        if (x1+y1) % 2 != 0 or (y2+x2) % 2 != 0:
            return -1
        #consider case 1: xx / yy
        #s1xx,s2yy
        c1 = min(x1//2,y2 // 2)
        #s1yy,s2xx
        c2 = min(y1//2,x2 // 2)
        cnt = c1 + c2
        x1 -= c1*2
        y2 -= c1*2
        x2 -= c2*2
        y1 -= c2*2
        cnt += (x1 + y1)
        return cnt

sol = Solution()
print(sol.minimumSwap("xyxyyx", "yxyxxy"))