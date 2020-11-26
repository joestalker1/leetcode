class Solution:
    def reverseVowels(self, s):
        vowles = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        i = 0
        chars = list(s)
        j = len(chars) - 1
        while i < j:
            while i < j and chars[i] not in vowles:
                i += 1
            while i < j and chars[j] not in vowles:
                j -= 1
            chars[i], chars[j] = chars[j], chars[i]
            i += 1
            j -= 1
        return ''.join(chars)

    