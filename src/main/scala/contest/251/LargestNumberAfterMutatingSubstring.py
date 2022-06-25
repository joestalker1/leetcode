class Solution:
    def maximumNumber(self, num: str, change):
        new_num = [int(num[i]) for i in range(len(num))]
        j = -1
        for i in range(len(num)):
            d = int(num[i])
            if change[d] > d:
                j = i
                break
        if j != -1:
            while j < len(num):
                d = int(num[j])
                if change[d] > d:
                    new_num[j] = change[d]
                else:
                    break
                j += 1

        return ''.join(list(map(str, new_num)))


sol = Solution()
print(sol.maximumNumber("334111",[0,9,2,3,3,2,5,5,5,5]))#"334999"
print(sol.maximumNumber(num = "132", change = [9,8,5,0,3,6,4,2,6,8]))