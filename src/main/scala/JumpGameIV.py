from collections import defaultdict

class Solution:
    def minJumps(self, arr) -> int:
        if len(arr) == 1 or arr[0] == arr[-1]:
            return 0 if len(arr) == 1 else 1
        num_to_index = defaultdict(list)
        for i in range(len(arr)):
            num_to_index[arr[i]].append(i)
        q = [0]
        min_len = 0
        last = len(arr) - 1
        seen = set()
        seen.add(0)
        while q:
            cur_num = len(q)
            for _ in range(cur_num):
                node = q.pop(0)
                if node == last:
                    return min_len
                if node + 1 <= last and (node + 1) not in seen:
                    q.append(node + 1)
                    seen.add(node + 1)
                if node - 1 >= 0 and (node - 1) not in seen:
                    q.append(node - 1)
                    seen.add(node - 1)
                a = arr[node]
                if len(num_to_index[a]) == 1:
                    continue
                for nei in num_to_index[a]:
                    if (nei == i or nei in seen) and nei != last:
                        continue
                    q.append(nei)
                    seen.add(nei)
            min_len += 1
        return -1


sol = Solution()
print(sol.minJumps([100,-23,-23,404,100,23,23,23,3,404]))#3