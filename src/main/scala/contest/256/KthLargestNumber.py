class Solution:
    def kthLargestNumber(self, nums, k: int) -> str:
        if len(nums) <= 1:
            return nums[0]

        def kthSmallest(arr, k, lo, hi):
            pivot = partition(arr, lo, hi)
            if pivot == k:
               return arr[k]
            if pivot > k:
               return kthSmallest(arr, k, lo, pivot - 1)
            return kthSmallest(arr, k, pivot + 1, hi)

        def partition(arr, lo, hi):
          p = arr[hi]
          i = lo - 1
          for j in range(lo, hi):
              if p < arr[j]:
                  i += 1
                  arr[i], arr[j] = arr[j], arr[i]
          arr[i + 1], arr[hi] = arr[hi], arr[i + 1]
          return i + 1

        max_len = len(max(nums,key=lambda x:len(x)))
        new_nums = [ '0' *(max_len - len(nums[i])) + nums[i] for i in range(len(nums))]
        num = str(kthSmallest(new_nums,k-1,0,len(nums) - 1))
        i = 0
        while i < len(num) and num[i] == '0':
            i += 1
        return num[i:]


sol = Solution()
print(sol.kthLargestNumber(["3","6","7","10"],4))#3