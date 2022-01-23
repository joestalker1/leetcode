import random

class Solution:

    def __init__(self, head):
        self.count = 0
        self.head = head
        p = head
        while p:
            self.count += 1
            p = p.next

    def getRandom(self) -> int:
        #choose reservoir sampling by size 1
        scope = 1
        choosen = None
        p = self.head
        while p:
            i = random.random()
            if i < 1/scope:
                choosen = p.val
            p = p.next
            #increase probality to replace choosen
            scope += 1
        return choosen
