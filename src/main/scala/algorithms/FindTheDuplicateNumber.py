class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # use 2 pointers: slow and fast
        slow = nums[0]
        fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if fast == slow:
                break
        #find entry point in cycle
        slow = nums[0]
        while slow != fast:
            fast = nums[fast]
            slow = nums[slow]
        return slow