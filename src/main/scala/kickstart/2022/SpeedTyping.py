def solve():
    t = int(input())
    for k in range(1, t + 1):
        I = input().strip()
        P = input().strip()
        i = 0
        j = 0
        while i < len(I) and j < len(P):
            if I[i] == P[j]:
                i += 1
                j += 1
            else:
                j += 1
        if i == len(I):
            print('Case #{}: {}\n'.format(k, len(P) - len(I)))
        else:
            print('Case #{}: IMPOSSIBLE\n'.format(k))


solve()
