
def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = list(map(int,input().split()))
        pre = [0] * (n + 1)
        jump = 0
        for i in range(n):
            #how many we have from the left to descrease current trampoline
            d = s[i] - pre[i] - 1
            if d > 0:
                #if it's left we should store the neccesary number to reducte the i trampoline to 1
                pre[i] = s[i] - 1
                # we can make it for jump
                jump += d
            else:
                # d <= 0 ,take -d and store it
                pre[i+1] += -d
            j = i + 2
            # distribute the s[i] to the right to use further.
            while j <= min(n-1, i + s[i]):
                pre[j] += 1
                j += 1
        print(jump)
solve()
