class Solution:
    def replaceNonCoprimes(self, nums):
        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)

        def lcm(a, b):
            gcd_of_two = gcd(a, b)
            return a * b // gcd_of_two

        new_nums = []
        for i in range(len(nums)):
            new_nums.append(nums[i])
            while len(new_nums) > 1 and gcd(new_nums[-1], new_nums[-2]) > 1:
                new_nums.append(lcm(new_nums.pop(), new_nums.pop()))
        return new_nums