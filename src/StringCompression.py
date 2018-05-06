class Solution:
    def compress(self, chars):
        i = 0
        r = 0
        while i < len(chars):
            count = 0
            j = i
            while j < len(chars) and chars[j] == chars[i]:
                count += 1
                j += 1

            chars[r] = chars[i]
            r += 1
            if count > 1:
                d = str(count)
                for ch in d:
                    chars[r] = ch
                    r += 1
            i = j
        return r


sol = Solution()
print(sol.compress(["a","a","a","a","a","b"]))
print(sol.compress(["a","a","b","b","c","c","c"]))
