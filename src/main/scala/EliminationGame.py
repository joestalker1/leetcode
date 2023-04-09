class Solution:
    def lastRemaining(self, n: int) -> int:
        if n == 1:
            return 1
        head = 1
        left = True
        rem = n
        step = 1
        while rem > 1:
            if left or rem % 2 == 1:
                head += step
            step *= 2
            rem = rem // 2
            left = not left
        return head

