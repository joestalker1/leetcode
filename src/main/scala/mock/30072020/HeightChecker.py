class Solution:
    def heightChecker(self, heights):
        if not heights:
            return 0
        for_photo = sorted(heights)
        count = 0
        for i in range(len(heights)):
            if for_photo[i] != heights[i]:
                count += 1
        return count