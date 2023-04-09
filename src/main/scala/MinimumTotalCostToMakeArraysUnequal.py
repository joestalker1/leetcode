class Solution:
    def minimumTotalCost(self, nums1, nums2) -> int:
        if not nums1 and not nums2:
            return False
        if not nums1:
            return True
        if not nums2:
            return True
        domin_val = -1
        domin_cnt = 0
        #number of bad numbers
        involved_cnt = 0
        min_cost = 0
        freq = defaultdict(int)
        for i in range(len(nums1)):
            if nums1[i] == nums2[i]:
                freq[nums1[i]] += 1
                if freq[nums1[i]] > domin_cnt:
                    domin_cnt = freq[nums1[i]]
                    domin_val = nums1[i]
                min_cost += i
                involved_cnt += 1
        if domin_cnt <= involved_cnt / 2:
            return min_cost
        for i in range(len(nums1)):
            if nums1[i] != nums2[i] and nums1[i] != domin_val and nums2[i] != domin_val:
                min_cost += i
                involved_cnt += 1
            if domin_cnt <= involved_cnt / 2:
                return min_cost
        return -1