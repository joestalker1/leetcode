from heapq import heappop,heappush,heapify

def solve():
    t = int(input())
    for i in range(1, t + 1):
        n = input()
        q = list(map(int, input().split()))
        heapify(q)
        max_streight = 0
        num = 1
        while q:
            a = heappop(q)
            if a >= num:
                max_streight += 1
                num += 1
        print('Case #{}: {}'.format(i, max_streight))


solve()