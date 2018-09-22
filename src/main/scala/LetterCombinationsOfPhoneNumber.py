class Solution:
    def __init__(self):
        self.num_to_chars = {"0": " ", "1":"","2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}

    def gen_comb(self, numbers, cur_digit, buf, result):
        if cur_digit == len(numbers):
            result.append(buf[:])
            return
        for ch in self.num_to_chars[numbers[cur_digit]]:
            if len(buf) == cur_digit:
                buf.append(ch)
            else:
                buf[cur_digit] = ch
            self.gen_comb(numbers, cur_digit+1, buf, result)

    def letterCombinations(self, digits):
        if not digits:
            return []
        result = []
        self.gen_comb(digits,0,[], result)
        return [''.join(list) for list in result]

sol = Solution()
print(sol.letterCombinations("23"))

