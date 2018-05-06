class Solution:
    def isPalindrome(self, s):
        s = s.strip().lower()
        if len(s) <= 1:
            return True
        i = 0
        j = len(s) - 1
        while i < j:
            if not s[i].isalnum():
                i += 1
            elif not s[j].isalnum():
                j -= 1
            else:
                if s[j] != s[i]:
                    return False
                i += 1
                j -= 1
        return True

sol = Solution()
print(sol.isPalindrome("...a..")) # true
print(sol.isPalindrome(".")) #true
print(sol.isPalindrome(" "))
print(sol.isPalindrome(".,"))#true
print(sol.isPalindrome("A man, a plan, a canal: Panama"))