class Solution:
    def minimumSize(self, nums, maxOperations):
        lo = 1
        hi = 10 ** 9

        def canDivide(sz):
            split = 0
            for b in nums:
                #count spilt number to spent to split this bag with balls
                split += (b - 1) // sz
                if split > maxOperations:
                    return False
            return True

        while lo < hi:
            #calculate balls for one bag
            sz = lo + (hi - lo) // 2
            #find leftmost max size that can't be used to split bags
            if canDivide(sz):
                # very big ball size,let decrease size
                hi = sz
            else:
                # too samll ball size to spilt bags,so increase size
                lo = sz + 1
        return lo


sol = Solution()
print(sol.minimumSize([431,922,158,60,192,14,788,146,788,775,772,792,68,143,376,375,877,516,595,82,56,704,160,403,713,504,67,332,26], 80))#129
print(sol.minimumSize([7,17], 2))#7
print(sol.minimumSize([2,4,8,2], 4))#2
print(sol.minimumSize([9], 2))#3





