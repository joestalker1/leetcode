class Solution:
    def shortestWay(self, source: str, target: str):
        if source == target:
            return 0

        i = 0
        parts = 0
        while i < len(target):
            parts += 1
            prev = i
            for j in range(len(source)):
                if source[j] == target[i]:
                    i += 1
            if prev == i:
                return -1
        return parts



