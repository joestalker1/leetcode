import itertools


class Solution(object):
    def slidingPuzzle(self, board):
        # convert 2 dim array to 1-dimension string
        s = ''.join([str(x) for x in list(itertools.chain(*board))])
        target = '123450'
        res = 0
        seen = set()
        # store the current board
        seen.add(s)
        q = [s]
        while q:
            # size of current all board variants
            sz = len(q)

            for _ in range(sz):
                v = q.pop(0)
                #if current board is desired target, return res
                if v == target:
                    return res
                i = v.index('0')
                # displacement of adjacent cells
                # 3 is column size
                for d in [1, -1, 3, -3]:
                    ni = i + d
                    # i and ni can't be neighbours
                    if ni < 0 or ni > 5 or i == 2 and ni == 3 or i == 3 and ni == 2:
                        continue
                    nv = list(v)
                    # swap 0 and new place
                    nv[i] = v[ni]
                    nv[ni] = '0'
                    ns = ''.join(nv)
                    if ns in seen:
                        continue
                    seen.add(ns)
                    q.append(ns)
            res += 1
        return -1


sol = Solution()
print(sol.slidingPuzzle([[4,1,2],[5,0,3]]))# 5
#print(sol.slidingPuzzle([[1,2,3],[5,4,0]])) #-1


