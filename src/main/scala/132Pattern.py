class Solution:
     def find132pattern(self, nums):
        if not nums:
            return False
        min_arr = [0] * len(nums)
        min_arr[0] = nums[0]
        for i in range(1, len(min_arr)):
            min_arr[i] = min(min_arr[i - 1], nums[i])#decreasing order
        stack = [] # for third element
        for i in range(len(nums) - 1,-1, -1):
            if nums[i] > min_arr[i]:
                while stack and stack[-1] <= min_arr[i]:
                    stack.pop()
                if stack and stack[-1] < nums[i]:
                    return True
                stack.append(nums[i])# nums[i] <= stack[-1]
        return False

sol = Solution()
print(sol.find132pattern([8,10,4,6,5]))#true
print(sol.find132pattern([3,5,0,3,4]))#true
print(sol.find132pattern([-1, 3, 2, 0]))#true
print(sol.find132pattern([1, 2, 3, 4]))#false
print(sol.find132pattern([3, 1, 4, 2]))#true