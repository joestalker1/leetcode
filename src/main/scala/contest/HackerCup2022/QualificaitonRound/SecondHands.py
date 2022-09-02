def solve():
    t = int(input())
    for i in range(1,t + 1):
        n,k = map(int, input().split())
        styles = map(int, input().split())
        if n > 2 * k:
            print(f'Case #{i}: NO')
        else:
            uniq = set()
            for s in styles:
                uniq.add(s)
            if len(uniq) < k:
                print(f'Case #{i}: NO')
            else:
                print(f'Case #{i}: YES')


solve()