class ImmutableListNode:
    def __init__(self, nums, cur):
        self.nums = nums
        self.cur = cur

    def printValue(self) -> None:
        print(self.nums[self.cur])

    def getNext(self) -> 'ImmutableListNode':
        if self.cur + 1 < len(self.nums):
            return ImmutableListNode(self.nums, self.cur + 1)
        return None


class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        if head is None:
            return
        self.printLinkedListInReverse(head.getNext())
        head.printValue()


list1 = ImmutableListNode([1,2,3,4], 0)
sol = Solution()
sol.printLinkedListInReverse(list1)

