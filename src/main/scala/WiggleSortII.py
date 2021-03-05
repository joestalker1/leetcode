class Solution:
    def wiggleSort(self, nums):
        def parition(s, e):
            i = s
            x = nums[e]
            for j in range(s, e):
                if nums[j] > x:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[e], nums[i] = nums[i], nums[e]
            return i

        def quick_select(s, e, k):
            # if k > 0 but [e - s+1]
            if 0 < k <= e - s + 1:
                # find p element
                p = parition(s, e)
                # if found K element, then return it.
                if p - s + 1 == k:
                    return nums[p]
                # otherwsie if k is in left part
                if p - s + 1 > k:
                    return quick_select(s, p - 1, k)
                # otherwise it is in right part
                # calculate delta (k - p - 1)
                return quick_select(p + 1, e, s + (k - p - 1))

        def mapInd(i):
            return (2 * i + 1) % (len(nums) | 1)

        n = len(nums)
        median = quick_select(0, n - 1, (n + 1) // 2)
        left = 0
        i = 0
        right = n - 1
        while i <= right:
            if nums[mapInd(i)] > median:
                nums[mapInd(left)],nums[mapInd(i)] = nums[mapInd(i)],nums[mapInd(left)]
                left += 1
                i += 1
            elif nums[mapInd(i)] < median:
                nums[mapInd(right)],nums[mapInd(i)] = nums[mapInd(i)],nums[mapInd(right)]
                right -= 1
            else:
                i += 1
        return nums


sol = Solution()
print(sol.wiggleSort([1,3,2,2,3,1]))#[2,3,1,3,1,2]

