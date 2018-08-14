# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):


def isBadVersion(version):
    return version >= 5

class Solution(object):
    def firstBadVersion(self, n):
        i = 1
        j = n + 1
        while i < j:
            version = (i + j) // 2
            if isBadVersion(version):
                j = version
            else:
                i = version + 1
        return i % (n + 1)

sol = Solution()
print(sol.firstBadVersion(5))


