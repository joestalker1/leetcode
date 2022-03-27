class Solution:
    def maximumEvenSplit(self, finalSum: int):

        def find_max_num_factor(cur_sum, num, lst, mem):
            if cur_sum in mem:
                return mem[cur_sum]
            if len(lst) == 0 and num > finalSum //2:
                return []
            if cur_sum < 0:
                return []
            if cur_sum == 0:
                return lst
            max_lst = []
            a = num
            # a is even
            while a <= cur_sum:
                cur_lst = find_max_num_factor(cur_sum - a, a + 2, lst + [a], mem)
                if len(max_lst) < len(cur_lst):
                    max_lst = cur_lst
                a += 2
            mem[cur_sum] = max_lst
            return max_lst

        max_lst = find_max_num_factor(finalSum, 2, [], {})
        return max_lst


sol = Solution()
print(sol.maximumEvenSplit(12))#[2,4,6]
print(sol.maximumEvenSplit(74416))#[2,4,6]