from math import inf

def solve():
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        arr = input().strip().split(' ')
        arr = [int(arr[i]) for i in range(n)]
        arr.sort()
        
        #find median

solve()

# 1
# 5
# 2 3 4 4 6