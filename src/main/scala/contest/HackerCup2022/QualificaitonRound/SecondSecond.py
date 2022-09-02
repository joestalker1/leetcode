from utils import read_file,write_file

def solve(buf):
    l = 0
    t = int(buf[l])
    l += 1
    res = []
    for k in range(1, t+1):
        r,c = map(int, buf[l].split())
        l += 1
        trees = set()
        rocks = set()
        for i in range(r):
            row = buf[l]
            l += 1
            for j in range(len(row)):
                if row[j] == '^':
                    trees.add((i,j))
                elif row[j] == '#':
                    rocks.add((i,j))

        def has_two_neighbours(rocks,land, x, y):
            if (x,y) in rocks:
                return False
            cnt = 0
            if x - 1 >= 0 and (x-1,y) not in rocks and (x-1, y) not in land:
                cnt += 1
            if x + 1 < r and (x + 1, y) not in rocks and (x + 1, y) not in land:
                cnt += 1
            if cnt < 2 and y - 1 >= 0 and (x,y-1) not in rocks and (x,y - 1) not in land:
                cnt += 1
            if cnt < 2 and y + 1 < c and (x,y+1) not in rocks and (x,y + 1) not in land:
                cnt += 1
            return cnt >= 2

        #proof that all trees may have at least 2 neighbours
        land = {}
        can_place = True
        for i in range(r):
            if not can_place:
                break
            for j in range(c):
                if (i,j) in rocks:
                    continue
                if (i,j) in trees:
                    if not has_two_neighbours(rocks, land, i, j):
                        can_place = False
                        break
                elif (i,j) in land:
                    continue
                else:
                    if not has_two_neighbours(rocks, land, i, j):
                        land[(i,j)] = 1

        if not can_place:
            res.append(f'Case #{k}: Impossible')
        else:
            res.append(f'Case #{k}: Possible')
            for i in range(r):
                row = []
                for j in range(c):
                    if (i,j) in rocks:
                        row.append('#')
                    elif (i,j) in land:
                        row.append('.')
                    else:
                        row.append('^')
                res.append(''.join(row))
    return res


path = '/Users/admin/Downloads/second_second_friend_input.txt'
buf = read_file(path)
res = solve(buf)
write_file('/Users/admin/output6.txt', res)