class Solution:
    def makesquare(self, nums):
        side = [0] * 4
        need_len = sum(nums) // 4

        def dfs(cur):
            if cur == len(nums):
                return True

            seen = set()
            for i in range(4):
                if side[i] in seen or side[i] + nums[cur] > need_len:
                    continue
                #if we have another side with same lenght
                seen.add(side[i])
                #if all sides are the same
                side[i] += nums[cur]
                if dfs(cur + 1):
                    return True
                # backtract length
                side[i] -= nums[cur]
            return False
        return dfs(0)

