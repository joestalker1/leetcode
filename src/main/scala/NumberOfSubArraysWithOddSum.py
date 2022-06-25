class Solution:
    def numOfSubarrays(self, nums) -> int:
        if not nums:
            return 0
        MOD = 10 ** 9 + 7
        cnt = 0
        odd_sum = 0
        even_sum = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                #all even summed become odd summed
                #all odd summed become even summed
                t = odd_sum
                odd_sum = even_sum + 1
                even_sum = t
            else:
                even_sum += 1
            cnt = (cnt % MOD + odd_sum % MOD) % MOD
        return cnt
