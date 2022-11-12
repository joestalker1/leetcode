class Solution:
    def nextBeautifulNumber(self, n: int) -> int:

        def next_perm(num):
            nums = list(str(num))
            i = len(nums) - 2
            while i >= 0 and nums[i] >= nums[i + 1]:
                i -= 1
            if i >= 0:
                j = len(nums) - 1
                while j >= 0 and nums[j] <= nums[i]:
                    j -= 1
                nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j = len(nums) - 1
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
            return int(''.join(nums))

        balanced_nums = [1, 22, 122, 333, 1333, 4444, 14444, 22333, 55555, 122333, 155555, 224444, 666666]
        s = str(n)
        smallest_bal_num = 1224444
        for num in balanced_nums:
            str_num = str(num)
            if len(s) > len(str_num):
                continue
            elif len(str_num) > len(s):
                smallest_bal_num = min(smallest_bal_num, num)
            else:
                nn = int(str_num)
                while True:
                    if nn > n:
                        smallest_bal_num = min(smallest_bal_num, nn)
                    nn = next_perm(nn)
                    if nn == num:
                        break
        return smallest_bal_num 