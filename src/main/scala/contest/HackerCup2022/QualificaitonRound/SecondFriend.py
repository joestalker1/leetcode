def solve():
    t = int(input())
    for k in range(1, t+1):
        r,c = map(int, input().split())
        trees = set()
        q = []
        for i in range(r):
            row = input().strip()
            for j in range(len(row)):
                if row[j] == '^':
                    trees.add((i,j))
                    q.append((i,j))
        can_place = True
        while q and can_place:
            cur_len = len(q)
            for _ in range(cur_len):
                i,j = q.pop(0)
                cnt = 0
                if i - 1 >= 0 and (i-1,j) in trees:
                    cnt += 1
                if i + 1 < r and (i+1,j) in trees:
                    cnt += 1
                if j - 1>=0 and (i,j-1) in trees:
                    cnt += 1
                if j + 1 < c and (i,j+1) in trees:
                    cnt += 1
                if cnt >= 2:
                    continue
                need_to_add = 2 - cnt
                if i - 1 >= 0 and (i - 1,j) not in trees:
                    q.append((i - 1,j))
                    trees.add((i - 1,j))
                    need_to_add -= 1
                if need_to_add > 0 and i + 1 < r and (i + 1, j) not in trees:
                    q.append((i + 1, j))
                    trees.add((i + 1, j))
                    need_to_add -= 1
                if need_to_add > 0 and j - 1 >= 0 and (i,j-1) not in trees:
                    q.append((i, j - 1))
                    trees.add((i, j - 1))
                    need_to_add -= 1
                if need_to_add > 0 and j + 1 < c and (i,j+1) in trees:
                    q.append((i, j + 1))
                    trees.add((i, j + 1))
                    need_to_add -= 1
                if need_to_add > 0:
                    can_place = False
                    break
        if not can_place:
            print(f'Case #{k}: Impossible')
        else:
            print(f'Case #{k}: Possible')
            for i in range(r):
                row = []
                for j in range(c):
                    if (i,j) in trees:
                        row.append('^')
                    else:
                        row.append('.')
                print(''.join(row))


solve()








