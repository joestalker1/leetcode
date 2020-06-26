class Solution:

    def numberToWords(self, num):

        def till_ten(n):
            t = {1: 'One',
                 2: 'Two',
                 3: 'Three',
                 4: 'Four',
                 5: 'Five',
                 6: 'Six',
                 7: 'Seven',
                 8: 'Eight',
                 9: 'Nine'}
            return t[n]

        def till_20(n):
            t = {
                10: 'Ten',
                11: 'Eleven',
                12: 'Twelve',
                13: 'Thirteen',
                14: 'Fourteen',
                15: 'Fifteen',
                16: 'Sixteen',
                17: 'Seventeen',
                18: 'Eighteen',
                19: 'Nineteen'
            }
            return t[n]

        def ten(n):
            t = {
                2: 'Twenty',
                3: 'Thirty',
                4: 'Forty',
                5: 'Fifty',
                6: 'Sixty',
                7: 'Seventy',
                8: 'Eighty',
                9: 'Ninety'
            }
            return t[n]

        def two(n):
            if not n:
                return ''
            if n < 10:
                return till_ten(n)
            elif n < 20:
                return till_20(n)
            else:
                t = n // 10
                rest = n - t * 10
                if t and rest:
                    return ten(t) + ' ' + till_ten(rest)
                return ten(t)

        def three(n):
            t = n // 100
            rest = n - t * 100
            if t and rest:
                return till_ten(t) + ' Hundred ' + two(rest)
            elif not t and rest:
                return two(rest)
            else:
                return till_ten(t) + ' Hundred'

        if not num:
            return 'Zero'

        billion = num // 1000000000
        million = (num - billion * 1000000000) // 1000000
        thousand = (num - billion * 1000000000 - million * 1000000) // 1000
        rest = num - billion * 1000000000 - million * 1000000 - thousand * 1000
        res = ''
        if billion:
            res += three(billion) + ' Billion'
        if million:
            res += ' ' if res else ''
            res += three(million) + ' Million'
        if thousand:
            res += ' ' if res else ''
            res += three(thousand) + ' Thousand'
        if rest:
            res += ' ' if res else ''
            res += three(rest)
        return res


sol = Solution()
print(sol.numberToWords(1000000))
print(sol.numberToWords(1234567))
print(sol.numberToWords(12345))
print(sol.numberToWords(123))
