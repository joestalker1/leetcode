def findBoggle(words, boggle):
    if not words and not boggle:
        return []

    res = []

    def dfs(word, i, row, col, visited, res):
        if i + 1 == len(word):
            res.append(word)
            return True
        for dr, dc in [[0, 1], [1, 0], [0, -1], [-1, 0], [1, 1], [-1, 1], [-1, -1], [1, -1]]:
            new_row = row + dr
            new_col = col + dc
            if 0 <= new_row < len(boggle) and 0 <= new_col < len(boggle[0]) and (new_row, new_col) not in visited and \
                    word[i + 1] == boggle[new_row][new_col]:
                visited.add((new_row, new_col))
                f = dfs(word, i + 1, new_row, new_col, visited, res)
                visited.discard((new_row, new_col))
                if f:
                    return True
        return False

    for word in words:
        visited = set()
        found = False
        for r in range(len(boggle)):
            if found:
                break
            for c in range(len(boggle[0])):
                if boggle[r][c] == word[0]:
                    visited.add((r, c))
                    found = dfs(word, 0, r, c, visited, res)
                    visited.discard((r, c))
                    if found:
                        break
    return res


print(findBoggle(["GEEKS", "FOR", "QUIZ", "GO"], [['G', 'I', 'Z'], ['U', 'E', 'K'], ['Q', 'S', 'E']]))
