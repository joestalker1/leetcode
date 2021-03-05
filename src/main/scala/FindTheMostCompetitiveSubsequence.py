class Solution:
    def mostCompetitive(self, nums, k):
        q = []
        addCount = len(nums) - k
        for a in nums:
            while q and q[-1] > a and addCount > 0:
                q.pop()
                addCount -= 1
            q.append(a)
        # q may contain more then k items
        return q[:k]
