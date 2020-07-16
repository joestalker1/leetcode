def isBadVersion(version):
    return version >= 9

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = 1
        e = n
        while s <= e:
            cand = s + (e - s)//2
            if isBadVersion(cand):
                e = cand - 1
            else:
                s = cand + 1
        return s

sol = Solution()
print(sol.firstBadVersion(10))

