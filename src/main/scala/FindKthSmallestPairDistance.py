from typing import List
import heapq, collections

def smallDistancePair(nums: List[int], k: int) -> int:
    """
    Function statement: return the pair's distance that is kth smallest
    Time complexity: O((n + k)log(n))
    Worst case: O(n^2log(n)) <- when k is large
    :param nums: all the possible pairing numbers
    :param k: target
    :return: kth smallest distance
    """
    # 1. Sort the nums array
    nums.sort()

    # 2. Get numbers' frequencies
    freq = collections.Counter(nums)
    keys = sorted(list(freq.keys()))

    # 3. Store n-1 sorted lists in a binary heap
    minHeap = [(keys[i + 1] - keys[i], i, i + 1) for i in range(len(keys) - 1)]
    heapq.heapify(minHeap)

    # 4. Count how many pairs' distance are 0
    cnt, rtn = 0, 0
    for key, val in freq.items():
        cnt += (val - 1) * val // 2

    # 5. Merge (len(nums) - 1) sorted lists
    while len(minHeap) > 0 and cnt < k:
        #  6. Pop the first k smallest pairs
        rtn, i, j = heapq.heappop(minHeap)
        k1, k2 = keys[i], keys[j]
        cnt += (freq[k1] * freq[k2])
        if j + 1 < len(keys):
            heapq.heappush(minHeap, (keys[j + 1] - keys[i], i, j + 1))

    # 7. Return the k-th smallest pair's distance
    return rtn

print(smallDistancePair([0, 0, 0, 0, 1, 1, 1, 2, 2, 2], k = 20))