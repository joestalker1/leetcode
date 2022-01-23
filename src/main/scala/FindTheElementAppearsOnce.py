class Solution:
    def getSingle(sel,arr):
        ones = 0
        twos = 0
        n = len(arr)
        for i in range(n):
            # one & arr[i]" gives the bits that
            # are there in both 'ones' and new
            # element from arr[]. We add these
            # bits to 'twos' using bitwise XOR
            twos = twos ^ (ones & arr[i])

            # one & arr[i]" gives the bits that
            # are there in both 'ones' and new
            # element from arr[]. We add these
            # bits to 'twos' using bitwise XOR
            ones = ones ^ arr[i]

            # The common bits are those bits
            # which appear third time. So these
            # bits should not be there in both
            # 'ones' and 'twos'. common_bit_mask
            # contains all these bits as 0, so
            # that the bits can be removed from
            # 'ones' and 'twos'
            common_bit_mask = ~(ones & twos)

            # Remove common bits (the bits that
            # appear third time) from 'ones'
            ones &= common_bit_mask

            # Remove common bits (the bits that
            # appear third time) from 'twos'
            twos &= common_bit_mask
        return ones


sol = Solution()
print(sol.getSingle([3, 3, 2, 3]))
