
class Solution:
    def nextGreatestLetter(self, letters, target):
        i = 0
        j = len(letters) - 1
        bisect.bi
        while i < j:
            mid = (i + j) // 2
            if letters[mid] > target:
                j = mid
            elif letters[mid] < target:
                i = mid + 1
        return letters[i % len(letters)]

sol = Solution()
#c
print(sol.nextGreatestLetter(["c", "f", "j"], "j"))
print(sol.nextGreatestLetter(["c", "f", "j"], "g"))
print(sol.nextGreatestLetter(["c", "f", "j"], "c"))
print(sol.nextGreatestLetter(["c", "f", "j"],"a"))