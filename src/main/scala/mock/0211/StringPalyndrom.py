class Solution(object):
    def isPalindrome(self, s):
        if not s:
            return True
        chars = []
        for ch in s:
            if 'a' <= ch <= 'z' or 'A' <= ch <= 'Z':
                chars.append(ch)
        new_s = ''.join(chars).lower()
        i = 0
        j = len(new_s) - 1
        while i < j:
            if new_s[i] != new_s[j]:
                return False
            i += 1
            j -= 1
        return True

sol = Solution()
print(sol.isPalindrome("race a car"))
print(sol.isPalindrome("A man, a plan, a canal: Panama"))
print(sol.isPalindrome(''))


