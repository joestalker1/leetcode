class Solution:
    def mostCompetitive(self, nums, k):
        if not nums or not k:
            return 0
        st = []
        n = len(nums)
        for i in range(n):
            while st and st[-1] > nums[i] and (len(st) + (n-i)) > k:
                st.pop()
            st.append(nums[i])
        return st[:k]


sol = Solution()
print(sol.mostCompetitive([71,18,52,29,55,73,24,42,66,8,80,2], 3))#[8,80,2]
print(sol.mostCompetitive([2,4,3,3,5,4,9,6], 4))#[2,3,3,4]
print(sol.mostCompetitive([3,5,2,6], 2))#[2,6]


