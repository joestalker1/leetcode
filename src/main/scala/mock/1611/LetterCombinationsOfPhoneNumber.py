class Solution(object):
    def letterCombinations(self, digits):
        if not digits:
            return []
        num_to_chars = {"0": " ", "1": "", "2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        def comb(i, res):
            if i == len(digits):
                return
            for ch in num_to_chars[digits[i]]:
                if not res:
                    res.append([ch])
                else:
                    if len(res[-1]) < (i + 1):
                        res[-1].append(ch)
                    else:
                        seq = res[-1][:i]
                        seq.append(ch)
                        res.append(seq)
                comb(i + 1, res)
        res = []
        comb(0, res)
        return [''.join(arr) for arr in res]

sol = Solution()
print(sol.letterCombinations("23"))

