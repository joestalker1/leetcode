class Solution:
    def maximumRemovals(self, s: str, p: str, removable) -> int:

        def is_subseq(k):
            rem_index = set(removable[:k])
            # index of p
            j = 0
            for i in range(len(s)):
                if i in rem_index or s[i] != p[j]:
                    continue
                if s[i] == p[j]:
                    j += 1
                if j == len(p):
                    return True
            return False

        lo = 1
        hi = len(removable)
        while lo < hi:
            k = lo + (hi - lo) // 2
            if is_subseq(k):
                lo = k + 1
            else:
                hi = k
        if not is_subseq(lo):
            lo -= 1
        return lo

sol = Solution()
print(sol.maximumRemovals(s = "abcacb", p = "ab", removable = [3,1,0]))#2
print(sol.maximumRemovals("qlevcvgzfpryiqlwy","qlecfqlw",[12,5]))#2