class Solution:
    def findRestaurant(self, list1, list2):
        rest = {}
        for i in range(len(list1)):
            k = list1[i]
            rest[k] = i
        min_sum = len(list1) + len(list2)
        res = list()
        for i in range(len(list2)):
            name = list2[i]
            if name in rest:
                j = rest[name]
                if min_sum > i + j:
                    min_sum = i + j
                    res = list()
                    res.append(name)
                elif min_sum == i+j:
                    res.append(name)
        return res


sol = Solution()
print(sol.findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"], ["KFC","Shogun","Burger King"]))
