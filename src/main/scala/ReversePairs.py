class Solution:
    def reversePairs(self, nums):
        cnt = 0

        def mergeSort(l, r):
            nonlocal cnt
            if l < r:
                m = l + (r - l) // 2
                left = mergeSort(l, m)
                right = mergeSort(m + 1, r)
                #merge and count rerversePair
                i = 0
                j = 0
                res = []
                while i < len(left) and j < len(right):
                    if left[i] > right[j]:
                        if left[i] > 2 * right[j]:
                            cnt += 1
                        res.append(right[j])
                        j += 1
                    elif left[i] < right[j]:
                        res.append(left[i])
                        i += 1
                    else:
                        res.append(left[i])
                        res.append(right[j])
                        i += 1
                        j += 1
                if i < len(left):
                    if len(right):
                        n = len(left) - i - 1
                        cnt += n*cnt
                    while i < len(left):
                        res.append(left[i])
                        i += 1
                while j < len(right):
                    res.append(right[j])
                    j += 1
                return res
            else:
                if 0 <= l< len(nums):
                    return [nums[l]]
                return []

        mergeSort(0, len(nums))
        return cnt


sol = Solution()
print(sol.reversePairs([2,4,3,5,1]))#3