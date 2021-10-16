from collections import defaultdict

class Solution:
    def countDifferentSubsequenceGCDs(self, nums) -> int:
        if not nums:
            return 0

        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)

        #fact = [0] * 200001
        fact = defaultdict(int)
        for i in range(len(nums)):
            for k in range(1, int(nums[i] ** 0.5) + 1):
                if nums[i] % k == 0:
                    fact1 = k
                    fact2 = nums[i] // fact1
                    fact[fact1] = gcd(fact[fact1], nums[i])
                    fact[fact2] = gcd(fact[fact2], nums[i])
        ans = 0
        for f,v in fact.items():
            if f == v:
                ans += 1
        return ans


sol = Solution()
print(sol.countDifferentSubsequenceGCDs([6,10,3]))