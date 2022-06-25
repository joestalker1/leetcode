def solve():
    t = int(input())
    for i in range(1, t+1):
        input()
        pancakes = list(map(int, input().split()))

        def serve(pancakes, l, r, prev, mem):
            if l > r:
                return 0
            k = '{}-{}-{}'.format(l,r,prev)
            if k in mem:
                return mem[k]
            max_cnt = 0
            if l <= r:
                if pancakes[l] >= prev:
                    max_cnt = 1 + serve(pancakes, l+1, r, pancakes[l], mem)
                else:
                    max_cnt = serve(pancakes, l+1, r, prev,mem)
            if r >= l:
                if pancakes[r] >= prev:
                    max_cnt = max(max_cnt, 1 + serve(pancakes, l, r-1, pancakes[r], mem))
                else:
                    max_cnt = max(max_cnt, serve(pancakes, l, r - 1, prev,mem))
            mem[k] = max_cnt
            return max_cnt
        mem = {}
        cnt = serve(pancakes, 0, len(pancakes)-1, 0, mem)
        print('Case #{}: {}'.format(i, cnt))

solve()