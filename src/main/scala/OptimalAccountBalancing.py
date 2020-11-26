from collections import defaultdict

class Solution:
    def minTransfers(self, transactions):
        balance = defaultdict(int)
        # calculate balance
        for s,e,m in transactions:
            balance[s] -= m
            balance[e] += m
        # filter money differ from 0
        lst = [v for k,v in balance.items() if v != 0]

        def dfs(start, lst):
            # if
            if start == len(lst):
                return 0
            # if some item is 0,it needs to go the end to get min_trans
            cur = lst[start]
            if cur == 0:
                return dfs(start + 1, lst)
            min_trans = float('inf')
            #try every start with every i, make all combination
            for i in range(start + 1, len(lst)):
                next = lst[i]
                # if item signs are different
                if cur * next < 0:
                    lst[i] = next + cur
                    min_trans = min(min_trans, 1 + dfs(start+1, lst))
                    lst[i] = next
                    if cur + next == 0:
                        break
            return min_trans
        return dfs(0, lst)

sol = Solution()
print(sol.minTransfers([[1,0,18],[2,1,9],[4,3,11],[5,4,10],[5,6,7],[7,6,5],[8,7,3]]))#6

print(sol.minTransfers([[10,11,6],[12,13,7],[14,15,2],[14,16,2],[14,17,2],[14,18,2]]))#6
print(sol.minTransfers([[0,1,2],[1,2,1],[1,3,1]]))#2
print(sol.minTransfers([[0,1,10], [1,0,1], [1,2,5], [2,0,5]]))#1
print(sol.minTransfers([[0,1,10], [2,0,5]]))#1





        





