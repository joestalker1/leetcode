class Solution:
    def minimizeTheDifference(self, mat, target: int) -> int:
        if not mat:
            return 0
        new_mat = defaultdict(list)
        for i in range(len(mat)):
            nums = set()
            for j in range(len(mat[0])):
                nums.add(mat[i][j])
            nums = list(nums)
            nums.sort()
            new_mat[i].extend(nums)

        dp = [[inf] * 4901 for _ in range(71)]

        def find_min_diff(mat, r, cur_sum, dp):
            if r >= len(mat):
                return abs(cur_sum - target)
            if dp[r][cur_sum] != inf:
                return dp[r][cur_sum]

            for num in mat[r]:
                dp[r][cur_sum] = min(dp[r][cur_sum], find_min_diff(mat, r + 1, cur_sum + num, dp))
                if dp[r][cur_sum] == 0 or cur_sum + num > target:
                    break
            return dp[r][cur_sum]

        return find_min_diff(new_mat, 0, 0, dp)

#TLE example how generate all possible sums
class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        if not mat:
            return 0
        bt = [False] * 4901
        max_val = 0
        min_diff = inf
        for k,row in enumerate(mat):
            bt1 = [False] * 4901
            max_val1 = 0
            for i in sorted(set(row)):
                for j in range(max_val + 1):
                    if j == max_val or bt[j]:
                        bt1[i+j] = True
                        max_val1 = max(max_val1, i + j)
                        if k == len(mat) - 1:
                            min_diff = min(min_diff,abs(i+j - target))
                            if (i + j) == target:
                                return abs(i + j - target)
            bt,bt1 = bt1,bt
            max_val = max_val1
        return min_diff