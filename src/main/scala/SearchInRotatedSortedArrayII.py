class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if len(nums) == 0:
            return False

        def is_bin_search(start, elm):
            return nums[start] != elm

        def exist_in_first(start, elm):
            return nums[start] <= elm

        lo = 0
        hi = len(nums) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] == target:
                return True
            if not is_bin_search(lo, nums[mid]):
                lo += 1
                continue
            piv = exist_in_first(lo, nums[mid])
            tr = exist_in_first(lo, target)

            if piv ^ tr:
                if piv:
                    lo = mid + 1
                else:
                    hi = mid - 1
            else:
                # pivot and target at the same half
                if nums[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid - 1
        return False
