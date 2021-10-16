from collections import defaultdict

t = int(input())

for i in range(1, t+1):
    n = int(input())
    grid = []
    for _ in range(n):
        s = input()
        s = s.strip()
        grid.append(s)
    rows = defaultdict(list)
    cols = defaultdict(list)
    row_hole = defaultdict(set)
    col_hole = defaultdict(set)
    for r in range(n):
        x = 0
        f = True
        for c in range(n):
            if grid[r][c] == 'O':
                f = False
            elif grid[r][c] == 'X':
                x += 1
            elif grid[r][c] == '.':
                row_hole[r].add((r,c))
        if f:
            rows[x].append(r)
    for c in range(n):
        f = True
        x = 0
        for r in range(n):
            if grid[r][c] == 'O':
                f = False
            elif grid[r][c] == 'X':
                x += 1
            elif grid[r][c] == '.':
                col_hole[c].add((r,c))
        if not f:
            continue
        cols[x].append(c)
    if len(rows) == 0 and len(cols) == 0:
        print('Case #{}: Impossible'.format(i))
    else:
        if len(rows) == 0:
            max_x = max(cols)
            min_num = n - max_x
            cases = len(cols)
        elif len(cols) == 0:
            max_x = max(rows)
            min_num = n - max_x
            cases = len(rows)
        else:
            max_x = max(max(rows),max(cols))
            min_num = n - max_x
            cases = 0
            if max(rows) == max_x:
                cases = len(rows[max_x])
                for c in cols[max_x]:
                    # find the same holes in cols
                    set1 = col_hole[c]
                    f = True
                    for r in rows[max_x]:
                        if row_hole[r] == set1:
                            f = False
                            break
                    if f:
                        cases += 1
            else:
                cases = len(cols[max_x])
                for r in rows[max_x]:
                    # find the same holes in cols
                    set1 = row_hole[r]
                    f = True
                    for c in cols[max_x]:
                        if col_hole[c] == set1:
                            f = False
                            break
                    if f:
                        cases += 1
        print('Case #{}: {} {}'.format(i, min_num, cases))
    print

# Case #1: 1 1
# Case #2: 1 2
# Case #3: 3 6
# Case #4: 2 2
# Case #5: 1 1
# Case #6: Impossible
# Case #7: 2 2
# Case #8: 1 2





