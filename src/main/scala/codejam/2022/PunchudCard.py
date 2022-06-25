def solve():
    t = int(input())
    for i in range(1, t+1):
        r,c = map(int, input().split())
        print('Case #{}:'.format(i))
        for i in range(2 * r + 1):
            line = []
            for j in range(2 * c + 1):
                if i == 0 and (j == 0 or j == 1) or i == 1 and (j == 0 or j == 1):
                    line.append('.')
                elif i % 2 == 0:
                    if j % 2 == 0:
                        line.append('+')
                    else:
                        line.append('-')
                elif i % 2 == 1:
                    if j % 2 == 0:
                        line.append('|')
                    else:
                        line.append('.')
            print('{}'.format(''.join(line)))


solve()




