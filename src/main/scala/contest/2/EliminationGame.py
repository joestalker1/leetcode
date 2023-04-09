import math


class Solution:
    def lastRemaining(self, n: int) -> int:
        if n == 1:
            return 1
        arr = [i for i in range(1,n+1)]
        print(*arr)
        p = int(math.log2(n))
        from_left = True
        l = 0
        r = 0
        for _ in range(p+1):
            if from_left:
                l = r
                if l > 1:
                    r *= 2
                #print(arr[l])
            else:
                if r <= 1:
                    r += 1
                else:
                    r *= 2
                l = r
                #print(arr[len(arr) - r-1])
            print('{},{}'.format(arr[l],arr[len(arr) - r-1]))
            from_left = not from_left
        return arr[-1]


sol = Solution()
#print(sol.lastRemaining(100))
#print(sol.lastRemaining(100000000))
#print(sol.lastRemaining(8))#6
#print(sol.lastRemaining(2))#1
#print(sol.lastRemaining(1))#1
print(sol.lastRemaining(9))#6