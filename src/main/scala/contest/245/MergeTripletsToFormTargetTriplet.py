from collections import defaultdict

class Solution:
    def mergeTriplets(self, triplets, target) -> bool:
        first_pos = defaultdict(list)
        second_pos = defaultdict(list)
        third_pos = defaultdict(list)
        for i, triplet in enumerate(triplets):
            a, b, c = triplet
            first_pos[a].append(triplet)
            second_pos[b].append(triplet)
            third_pos[c].append(triplet)
        common = [first_pos, second_pos, third_pos]
        x, y, z = target
        if x not in first_pos or y not in second_pos or z not in third_pos:
            return False

        def dfs(common, cur_num, start_triplet):
            if cur_num == 3:
                return True
            for triplet in common[cur_num][target[cur_num]]:
                new_triplet = [max(start_triplet[0], triplet[0]), max(start_triplet[1], triplet[1]),
                               max(start_triplet[2], triplet[2])]
                matched = True
                for i in range(cur_num + 1):
                    if new_triplet[i] != start_triplet[i] or new_triplet[i] != target[i]:
                        matched = False
                        break
                if matched:
                    if dfs(common, cur_num + 1, new_triplet):
                        return True
            return False

        for triplet in common[0][target[0]]:
            if dfs(common, 0, triplet):
                return True
        return False


sol = Solution()
print(sol.mergeTriplets([[2,5,3],[1,8,4],[1,7,5]],[2,7,5]))