from collections import defaultdict

class Solution:
    def canPartitionKSubsets(self, nums, k):
        arr_sum = sum(nums)
        need_sum = arr_sum // k
        subset = [0] * k

        def dfs(cur):
            if cur == len(nums):
                return True
            m = defaultdict(int)
            for i in range(k):
                if subset[i] in m:
                    if m[subset[i]]:
                        return True
                    else:
                        continue
                if subset[i] + nums[cur] > need_sum:
                    continue
                subset[i] += nums[cur]
                res = dfs(cur + 1)
                subset[i] -= nums[cur]
                m[subset[i]] = res
                if res:
                    return True
            return False
        return dfs(0)


sol = Solution()
print(sol.canPartitionKSubsets([724,3908,1444,522,325,322,1037,5508,1112,724,424,2017,1227,6655,5576,543], 4))#True
#print(sol.canPartitionKSubsets([4, 3, 2, 3, 5, 2, 1], 4))#True
#print(sol.canPartitionKSubsets([1,2,3,4],3))#False



