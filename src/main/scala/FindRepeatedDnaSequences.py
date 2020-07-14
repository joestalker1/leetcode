class Solution:
    def findRepeatedDnaSequences(self, s):
        L, n = 10, len(s)
        if L == len(s):
            return s
        a = 4
        aL = pow(a, L)
        to_int = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        nums = [to_int.get(s[i]) for i in range(len(s))]
        h = 0
        out = set()
        seen = set()

        for i in range(len(nums) - L + 1):
            if i != 0:
                h = h * a - nums[i - 1] * aL + nums[i + L - 1]
            else:
                for j in range(L):
                    h = h * a + nums[j]
            if h in seen:
                out.add(s[i:i + L])
            seen.add(h)
        return out


sol = Solution()
print(sol.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))

