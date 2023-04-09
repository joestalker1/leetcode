from collections

class Solution:
    def countDistinct(self, nums, k: int, p: int) -> int:
        if not nums or p == 0:
            return 0
        #store number of nums is divisibleby  k
        cnt = [0] * 201
        #hash value of nums starts from nums[i]
        hash = [0] * 201
        MOD = 10 ** 7
        subarr_cnt = 0

        def check_collision(arr,s,e):
            k = s
            for j in arr:
                if k > e:
                    break
                if nums[j] == nums[k]:
                    return True
                k += 1
            return False

        for sz in range(len(nums)):
            i = 0
            #hash to subsarray
            uniq_arr = collections.defaultdict(list)
            while i + sz < len(nums):
                cnt[i] += (1 if nums[i + sz] % p == 0 else 0)
                if cnt[i] <= k:
                    hash[i] = (hash[i] * 131 + nums[i + sz]) % MOD
                    if not check_collision(uniq_arr[hash[i]], i,i + sz):
                        uniq_arr[hash[i]].append(i)
                        subarr_cnt += 1
                i += 1
        return subarr_cnt

#[2], [2,3], [2,3,3], [2,3,3,2], [3], [3,3], [3,3,2], [3,3,2,2], [3,2], [3,2,2], and [2,2]
sol = Solution()
print(sol.countDistinct([2,3,3,2,2],2,2))#11
print(sol.countDistinct([1,2,3,4], 4,1))#10