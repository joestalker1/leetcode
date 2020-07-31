from collections import defaultdict

class Solution:
    def totalFruit(self, tree):
        if not tree:
            return 0
        buskets = defaultdict(int)
        max_total = 0
        left = 0
        for right in range(len(tree)):
            buskets[tree[right]] += 1
            while len(buskets.keys()) > 2 and left < right:
                buskets[tree[left]] -= 1
                max_total = max(max_total,right - left)
                if buskets[tree[left]] == 0:
                    buskets.pop(tree[left])
                left += 1

        while len(buskets.keys()) > 2 and left < right:
            buskets[tree[left]] -= 1
            max_total = max(max_total,right - left)
            if buskets[tree[left]] == 0:
                buskets.pop(tree[left])
            left += 1
        return max_total


