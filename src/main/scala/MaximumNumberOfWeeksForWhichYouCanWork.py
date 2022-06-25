class Solution:
    def numberOfWeeks(self, milestones) -> int:
        if len(milestones) == 1:
            return 1
        total = sum(milestones)
        return min(2*(total - max(milestones)) + 1, total)