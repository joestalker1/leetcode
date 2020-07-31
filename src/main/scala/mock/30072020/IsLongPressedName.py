class Solution:
    def isLongPressedName(self, name, typed):
        if not name and not typed or name == typed:
            return True
        if not name or not typed:
            return False
        i = 0
        groups = []
        while i < len(name):
            j = i
            while j < len(name) and name[j] == name[i]:
                j += 1
            groups.append([name[i], j - i])
            i = j
        i = 0
        while i < len(typed):
            j = i
            while j < len(typed) and typed[j] == typed[i]:
                j += 1
            c = j - i
            ch = typed[i]
            i = j
            if len(groups) == 0:
                return False
            exp = groups.pop(0)
            if ch != exp[0] or c < exp[1]:
                return False
        return len(groups) == 0


sol = Solution()
print(sol.isLongPressedName("alex", "aaleex"))



