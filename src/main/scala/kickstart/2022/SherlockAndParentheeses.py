def solve():
    t = int(input())
    for k in range(1,t+1):
        l,r = map(int, input().split())
        n = l + r
        balanced_string = 0
        for s in range(1, 2**n):
            m = n
            cur_balanced_strings = 0
            while m > 0:
                # n = 4, 2 ** 4 - 1 = 15
                h = s & (2**m-1)
                cnt = 0
                for j in range(m-1, -1, -1):
                    if (h & (1 <<j)) != 0:
                        cnt += 1
                    else:
                        cnt -= 1
                    if cnt < 0:
                        break
                    if cnt == 0:
                        cur_balanced_strings += 1
                m -= 1
            balanced_string = max(balanced_string, cur_balanced_strings)
        print(f"Case #{k}: {balanced_string}")

solve()

