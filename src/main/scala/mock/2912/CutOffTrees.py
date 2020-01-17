class Solution(object):
    def cutOffTree(self, forest):
        if not forest:
            return []
        height_to_tree = {}
        for r in range(forest):
            for c in range(forest[0]):
                h = forest[r][c]
                if h > 1:
                    height_to_tree[h] = [r,c]
        min_height = min(height_to_tree.keys())
        max_height = max(height_to_tree.keys())

        def dfs(r,c, target, seen):
            if (r,c) in seen:
                return float('inf')
            if r == target[0] and c == target[1]:
                return 0
            seen.add(())
            min_path
            if r +1 < len(forest) and forest[r+1][c] != 0:


        for h in range(max_height, max_height + 1):




