class Solution(object):
    def rotate(self):
        rotate = [i for i in range(10)]
        rotate[1] = 1
        rotate[8] = 8
        rotate[2] = 5
        rotate[5] = 2
        rotate[6] = 9
        rotate[9] = 6
        return rotate

    def valid(self, dig1, dig2):
        bad_dig = set([3, 4, 7])
        c = 0
        for i in range(len(dig1)):
            if dig1[i] in bad_dig:
                return False
            if dig1[i] == dig2[i]:
                c += 1
        if c == len(dig1):
            return False

        return True

    def rotatedDigits(self, N):
        mapt = self.rotate()
        count = 0
        for a in range(N + 1):
            digits1 = []
            digits2 = []
            while a > 0:
                rem = a % 10
                digits1.append(rem)
                rot = mapt[rem]
                digits2.append(rot)
                a = a // 10
            if self.valid(digits1, digits2):
                count += 1
        return count


sol = Solution()
print(sol.rotatedDigits(847))
