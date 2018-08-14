class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x = 0
        for i in nums:
            x = x ^ i
        return x


def main():
    s = Solution()
    print(s.singleNumber([1,3,1,3,2]))


if __name__ == "__main__":
    main()
