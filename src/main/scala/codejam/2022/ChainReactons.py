from collections import defaultdict

def solve():
    t = int(input())
    for k in range(1, t + 1):
        n = int(input())
        #start from 1
        fun = list(map(int, input().split()))
        fun = [0] + fun
        #0 is abys,all index is from 1
        next_node = list(map(int, input().split()))
        next_node = [0] + next_node

        #find all leaves and put them into min heap
        leaves = [1] * (n+1)
        for i in range(1, n + 1):
            n = next_node[i]
            leaves[n] = 0

        max_fun = 0
        for v in range(1, n+1):
            if leaves[v] == 1 and next_node[v] == 0:
                max_fun += fun[v]
                leaves[v] = 0

        mem = defaultdict(int)

        #call for one chain reaction
        def chain(next_node, fun, v, used):
            if v == 0 or ((used >> v) & 1) == 1:
                return 0, used
            used |= 1 << v
            (cur_fun, used2) = chain(next_node, fun, next_node[v], used)
            if cur_fun > fun[v]:
                return cur_fun, used2
            return fun[v], used2

        def backtrack(next_node, fun, used, mem):
            max_fun = 0
            if used in mem:
                return mem[used]
            for v in range(1, n + 1):
                if leaves[v] == 0 or ((used >> v) & 1) == 1:
                    continue
                (cur_fun, used2) = chain(next_node, fun,v, used)
                cur_fun += backtrack(next_node, fun, used2, mem)
                max_fun = max(max_fun, cur_fun)
            mem[used] = max_fun
            return max_fun

        max_fun += backtrack(next_node, fun, 0,mem)
        print('Case #{}: {}'.format(k, max_fun))


solve()