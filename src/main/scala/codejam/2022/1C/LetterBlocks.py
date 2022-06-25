from math import inf

def solve():
    t = int(input())
    for i in range(1, t + 1):
        input()
        tower = input().split()

        def intersect(s1, s2):
            uniq1 = set(s1)
            uniq2 = set(s2)
            return len(uniq1.intersection(uniq2))

        def is_proper(s):
            used = {}
            for i in range(len(s)):
                if s[i] in used and used[s[i]] != i - 1:
                    return False
                used[s[i]] = i
            return True


        def compose(tower,mega_tower, used_block):
            if len(mega_tower) == len(tower):
                return mega_tower
            for blk in range(len(tower)):
                if (1 << blk) & used_block:
                    continue
                # if mega_tower and tower[blk][0] != mega_tower[-1][-1] and tower[blk][-1] != mega_tower[0][0] and intersect(tower[blk],''.join(mega_tower)):
                #     continue
                # if mega_tower and (tower[blk][0] == mega_tower[-1][-1] or tower[blk][-1] == mega_tower[0][0]) and get_used_char(tower[blk]) & used_char:
                #     continue
                if not mega_tower:
                    res = compose(tower, mega_tower +[tower[blk]],(1 << blk) | used_block)
                    if res:
                        return res
                else:
                    if tower[blk][0] == mega_tower[-1][-1] and intersect(tower[blk],  mega_tower[-1]) == 1 and intersect(tower[blk],mega_tower[0:-1]) == 0:
                        res = compose(tower, mega_tower + [tower[blk]], (1 << blk) | used_block)
                        if res:
                            return res
                    elif tower[blk][-1] == mega_tower[0][0] and intersect(tower[blk],  mega_tower[0]) == 1 and intersect(tower[blk], mega_tower[1:]) == 0:
                        res = compose(tower, [tower[blk]] + mega_tower, (1 << blk) | used_block)
                        if res:
                            return res
                    elif intersect(tower[blk], ''.join(mega_tower)) == 0:
                        res = compose(tower, mega_tower + [tower[blk]], (1 << blk) | used_block)
                        if res:
                            return res
                        res = compose(tower, [tower[blk]] + mega_tower, (1 << blk) | used_block)
                        if res:
                            return res
            return None

        bad = False
        for s in tower:
            if not is_proper(s):
                print('Case #{}: IMPOSSIBLE'.format(i))
                bad = True
                break
        if not bad:
            res = compose(tower, [], 0)
            if res:
                print('Case #{}: {}'.format(i, ''.join(res)))
            else:
                print('Case #{}: IMPOSSIBLE'.format(i))

solve()