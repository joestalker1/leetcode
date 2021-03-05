class Solution:
    def canChoose(self, groups, nums):

        def find_group(group, last_j):
            if last_j + len(group) > len(nums):
                return -1
            i = 0
            for j in range(last_j, len(nums)):
                if group[i] == nums[j]:
                    break
            if j == len(nums):
                return -1
            # the left should equal ther rest of nums
            i += 1
            res = j
            j += 1
            while i < len(group) and j < len(nums) and group[i] == nums[j]:
                j += 1
                i += 1
            if i == len(group):
                # cool subarray for group
                return res
            return find_group(group,last_j + 1)

        def find_groups(groups):
            pos = 0
            for group in groups:
                pos = find_group(group, pos)
                if pos == -1:
                    return False
                pos += len(group)
            return True
        return find_groups(groups)


sol = Solution()
print(sol.canChoose([[1,-1,-1],[3,-2,0]], [1,-1,0,1,-1,-1,3,-2,0]))


