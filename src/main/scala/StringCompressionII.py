class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        if not s:
            return len(s)

        @lru_cache(None)
        def find_min_run_len(i, last_char, last_char_cnt, k):
            if k < 0:
                return math.inf
            if i == len(s):
                return 0
            delete_char = find_min_run_len(i + 1, last_char, last_char_cnt, k - 1)
            if last_char == s[i]:
                # if char cnt is one we don't use run_len encoding like 1a,
                # if char cnt is 9, that encoding takes by one more,
                # if char cnt is 99, it's as above.
                keep_char = find_min_run_len(i + 1, last_char, last_char_cnt + 1, k) + (last_char_cnt in [1, 9, 99])
            else:
                keep_char = find_min_run_len(i + 1, s[i], 1, k) + 1
            return min(delete_char, keep_char)

        return find_min_run_len(0, '', 0, k)


sol = Solution()
print(sol.getLengthOfOptimalCompression("aabbaa", 2))