class Solution:
    def nextGreaterElements(self, nums):
        if not nums:
            return []
        res = []
        val_index = [(a, i) for i, a in enumerate(nums)]
        val_index.sort(key=lambda x: [x[0], x[1]])

        def find(a):
            s = 0
            e = len(val_index) - 1
            while s < e:
                m = s + (e - s) // 2
                if val_index[m][0] > a:
                    e = m
                else:
                    s = m + 1
            return val_index[s][1] if s <= e else -1

        for i, a in enumerate(nums):
            k = find(a)
            if k == i or k == -1:
                res.append(-1)
            elif 0 <= k < i:
                l = 0
                while nums[l] <= a and l <= k:
                    l += 1
                res.append(nums[l])
            else:
                res.append(nums[k])
        return res


sol = Solution()
print(sol.nextGreaterElements([1, 5, 3, 6, 8]))
print(sol.nextGreaterElements([5, 4, 3, 2, 1]))
print(sol.nextGreaterElements([3, 2, 1]))
print(sol.nextGreaterElements([1, 2, 1]))
