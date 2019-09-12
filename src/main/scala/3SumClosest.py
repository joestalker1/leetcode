class Solution:
    def threeSumClosest(self, nums, target):
        if not nums or len(nums) < 3:
            return None
        nums.sort()
        closest = sum(nums[:3])
        for i in range(len(nums) - 2):
            s = i + 1
            e = len(nums) - 1
            while s < e:
                candidate = nums[i] + nums[s] + nums[e]
                if abs(target - candidate) < abs(target - closest):
                    closest = candidate

                if candidate > target:
                    e -= 1
                elif candidate < target:
                    s += 1
                else:
                    return target
        return closest

sol = Solution()
print(sol.threeSumClosest([1,1,1,0], -100))#2
print(sol.threeSumClosest([0, 1, 2], 3))#3
print(sol.threeSumClosest([1,2,3], 1))
print(sol.threeSumClosest([-1, 2, 1, -4], 1))


