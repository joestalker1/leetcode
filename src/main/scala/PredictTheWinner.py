class Solution:

    def PredictTheWinner(self, nums):
        def win(s, e, mem):
            if s == e:
                return nums[s]
            if (s, e) in mem:
                return mem[(s, e)]
            # we subtract scores from nums[s] as win of other player
            # pick either leftmost or rightmost item
            a = nums[s] - win(s + 1, e, mem)
            b = nums[e] - win(s, e - 1, mem)
            # choose max profit
            best = max(a, b)
            mem[(s,e)] = best
            return mem[(s,e)]
        mem = {}
        # if profit >=0, player 1 wins
        return win(0, len(nums) - 1, mem) >= 0


sol = Solution()
# print(sol.PredictTheWinner([9337301,0,2,2245036,4,1997658,5,2192224,960000,1261120,8824737,1,1161367,9479977,7,2356738,5,4,9])) #true
# print(sol.PredictTheWinner([1,1,1]))#true
# print(sol.PredictTheWinner([1, 1, 567, 1, 1, 99]))  # true
# print(sol.PredictTheWinner([1, 5, 2]))  # false
# print(sol.PredictTheWinner([1, 2, 3, 4, 999, 3]))  # true
# print(sol.PredictTheWinner([1, 2, 99]))  # true
print(sol.PredictTheWinner([1, 5, 233, 7]))  # true
# print(sol.PredictTheWinner([2, 2, 454, 2, 2]))  # false
