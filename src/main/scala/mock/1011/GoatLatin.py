class Solution(object):
    def toGoatLatin(self, S):
        if not S:
            return ''
        goat_latin = []
        suffix = 'a'
        for word in S.split(' '):
            if word[0].lower() in 'aeiou':
                goat_latin.append(word[:]+'ma' + suffix)
            else:
                goat_word = word[1:] + word[0] + 'ma' + suffix
                goat_latin.append(goat_word)
            suffix += 'a'
        return ' '.join(goat_latin)


sol = Solution()
print(sol.toGoatLatin("The quick brown fox jumped over the lazy dog"))
print(sol.toGoatLatin("I speak Goat Latin"))#"Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
