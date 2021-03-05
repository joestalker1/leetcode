class Solution:
    def countLetters(self, S: str) -> int:
        #count of substrings ending at i
        #if one char is 1 substring
        count = 1
        total = count
        for i in range(1, len(S)):
            #if current char is as previois, let increment current count of substring ending at 1
            if S[i] == S[i-1]:
                count = count + 1
            else:
                # set number of substrings to 1
                count = 1
            total += count
        #count total number of all substring with one character
        return total

sol = Solution()
print(sol.countLetters("aaa"))