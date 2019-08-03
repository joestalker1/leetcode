class Solution:
    def twoSum(self, nums, target, start, end):
        res = []
        i = start
        j = end
        while i < j:
            sum_of_two = nums[i] + nums[j]
            if sum_of_two > target:
                j -= 1
            elif sum_of_two < target:
                i += 1
            else:
                res.append([nums[i], nums[j]])
                i += 1
                j -= 1
                while i < j and nums[i] == nums[i - 1]:
                    i += 1
                while i < j and nums[j] == nums[j + 1]:
                    j -= 1

        return res

    def threeSum(self, nums, target, start, end):
        res = []
        for j in range(start, end - 1):
            rest = target - nums[j]
            candidates = self.twoSum(nums, rest, j + 1, len(nums) - 1)
            if len(candidates) > 0:
                # [[a,b],[c,d]]
                # flatten it
                for a,b in candidates:
                    res.append([nums[j], a, b])
        return res

    def hash(self, list_of_nums):
        h = 11 * list_of_nums[0]
        for i in range(1, len(list_of_nums)):
            h += list_of_nums[i]
        return h

    def has_dup(self, nums, list_of_nums):
        for num in nums:
            if num == list_of_nums:
                return True
        return False

    def fourSum(self, nums, target):
        nums.sort()
        res = {}
        neg_res = set()
        for i in range(len(nums) - 3):
            rest = target - nums[i]
            if rest in neg_res:
                continue
            candidates = self.threeSum(nums, rest, i + 1, len(nums) - 1)
            if len(candidates) > 0:
                #[[a,b,c],[e,f,g]]
                for a,b,c in candidates:
                    hash = self.hash([a, b, c])
                    if hash in res:
                        if self.has_dup(res[hash], [nums[i], a,b,c]):
                            continue
                    if hash not in res:
                        res[hash] = []
                    res[hash].append([nums[i], a,b,c])
            else:
                neg_res.add(rest)
        return list([item for k,items in res.items() for item in items])


sol = Solution()
print(sol.fourSum([-494,-474,-425,-424,-391,-371,-365,-351,-345,-304,-292,-289,-283,-256,-236,-236,-236,-226,-225,-223,-217,-185,-174,-163,-157,-148,-145,-130,-103,-84,-71,-67,-55,-16,-13,-11,1,19,28,28,43,48,49,53,78,79,91,99,115,122,132,154,176,180,185,185,206,207,272,274,316,321,327,327,346,380,386,391,400,404,424,432,440,463,465,466,475,486,492],-1211))
#print(sol.fourSum([-3,-2,-1,0,0,1,2,3],0))
#print(sol.fourSum([-497,-488,-484,-462,-453,-422,-402,-378,-371,-362,-345,-342,-332,-301,-290,-257,-239,-229,-205,-175,-98,-92,-90,-87,-73,-67,-63,-61,-40,-37,-36,-32,-16,-10,0,33,45,53,110,110,130,147,174,194,207,218,221,247,249,260,273,278,311,323,335,356,357,371,421,432,455,482,487], 4941))
#print(sol.fourSum([-463,-428,-392,-386,-348,-312,-280,-248,-247,-244,-224,
#                   -216,-198,-195,-195,-189,-175,-173,-167,-155,-111,-96,-36,-28,-3,10,15,22,25,44,44,49,50,68,84,88,104,107,111,116,171,208,233,304,309,313,318,323,330,331,331,358,364,365,388,396,403,425,449], 2110))
#print(sol.fourSum([0,0,0,0], 0))
print(sol.fourSum([1, 0, -1, 0, -2, 2], 0))


