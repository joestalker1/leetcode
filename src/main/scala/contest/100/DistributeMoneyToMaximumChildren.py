class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if money < children:
            return -1
        if money <= 8 and children > 1 or money - 8 < children - 1:
            return 0
        possible_children = money // 8
        possible_children = min(possible_children, children)
        if money - 8*possible_children > 0 and possible_children >= children:
            return children - 1
        rest = money % 8
        if rest == 4:
            #need to find 2 children
            left = children - possible_children
            possible_children -= max(0, 2 - left)
        elif rest > 0 and possible_children == children:
             possible_children -= 1
        if money - 8 * possible_children < children - possible_children:
            while money - 8 * possible_children < children - possible_children:
                possible_children -= 1
        return max(possible_children, 0)

sol = Solution()
print(sol.distMoney(24,11) == 1)
print(sol.distMoney(20,2) == 1)
print(sol.distMoney(17, 4) == 1)
print(sol.distMoney(12,3) == 1)
print(sol.distMoney(9, 3) == 0)
print(sol.distMoney(16,2) == 2)
print(sol.distMoney(1,2) == -1)
print(sol.distMoney(4,3) == 0)
print(sol.distMoney(16,3) == 1)
print(sol.distMoney(20,3) == 1)
print(sol.distMoney(9,2) == 1)#1