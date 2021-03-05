class Solution:
    def halvesAreAlike(self, s: str):
        vowels = set('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        part1 = s[0:len(s) // 2]
        part2 = s[len(s) // 2:]

        def count_vowel(part):
            return len([ch for ch in part if ch in vowels])
        return count_vowel(part1) == count_vowel(part2)

