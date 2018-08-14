class Solution:
    def reverseSubstring(self, str, start, end):
        while start < end:
            str[start],str[end] = str[end],str[start]
            start += 1
            end -= 1

    def reverseWords(self, str):
        if not str:
            return
        self.reverseSubstring(str, 0, len(str) - 1)
        i = 0
        while i < len(str):
            j = i + 1
            while j < len(str) and str[j] != ' ':
                j += 1
            j -= 1
            self.reverseSubstring(str, i, j)
            i = j + 2

sol = Solution()
arr = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
sol.reverseWords(arr)
print(arr)