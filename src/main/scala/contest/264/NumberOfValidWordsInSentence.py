class Solution:
    def componentValue(self, nums: List[int], edges: List[List[int]]) -> int:
        if not nums or not edges:
            return 0
        sum_of_arr = sum(nums)

        # every divisor may be component sum
        degree = [0] * len(nums)
        adj_list = defaultdict(set)
        for a, b in edges:
            adj_list[a].add(b)
            adj_list[b].add(a)
            degree[a] += 1
            degree[b] += 1

        def find_component(adj_list, comp_sum):
            deg = degree[:]
            vals = nums[:]
            queue = [i for i, d in enumerate(deg) if d == 1]
            while queue:
                node = queue.pop(0)
                deg[node] = 0
                for nei in adj_list[node]:
                    if vals[node] != comp_sum:
                        vals[nei] += vals[node]
                    deg[nei] -= 1
                    if deg[nei] == 0:
                        return vals[nei] == comp_sum
                    elif deg[nei] == 1:
                        queue.append(nei)
            return False

        for comp_sum in range(min(nums), sum_of_arr):
            if sum_of_arr % comp_sum == 0 and find_component(adj_list, comp_sum):
                # if every component is comp_sum,they are tied with sum_of_arr // comp_sum - 1 edges.
                return sum_of_arr // comp_sum - 1
        return 0


sol = Solution()
print(sol.countValidWords('!'))#1
print(sol.countValidWords("!this  1-s b8d!"))#0
print(sol.countValidWords("he bought 2 pencils, 3 erasers, and 1  pencil-sharpener."))#6
print(sol.countValidWords("alice and  bob are playing stone-game10"))
print(sol.countValidWords('!this  1-s b8d!'))#0