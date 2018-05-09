import itertools
class Solution:
    def intersect(self, nums1, nums2):
        if len(nums1) == 0:
            return False
        if len(nums2) == 0:
            return False
        dict1 = {}
        for i in range(len(nums1)):
            if nums1[i] in dict1:
                c = dict1[nums1[i]]
                dict1[nums1[i]] = c + 1
            else:
                dict1[nums1[i]] = 1

        dict2 = {}
        for i in range(len(nums2)):
            if nums2[i] in dict2:
                c = dict2[nums2[i]]
                dict2[nums2[i]] = c + 1
            else:
                dict2[nums2[i]] = 1

        if len(dict1) < len(dict2):
            for k,v in dict1.items():
                if k in dict2:
                    c = dict2[k]
                    if c < v:
                        dict1[k] = c
                else:
                    del dict1[k]
            return list(itertools.chain.from_iterable([[k] * v for k,v in dict1.items()]))
        else:
            for k,v in dict2.items():
                if k in dict1:
                    c = dict1[k]
                    if c < v:
                        dict2[k] = c
                else:
                    del dict2[k]
            return list(itertools.chain.from_iterable([[k] * v for k,v in dict2.items()]))

nums1 = [1,2,2,1]
nums2 = [2,2,1]
sol = Solution()
print(sol.intersect(nums1, nums2))