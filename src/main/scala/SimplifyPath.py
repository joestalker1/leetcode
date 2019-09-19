class Solution:
    def simplifyPath(self, path):
        if not path:
            return None
        can_path = []
        parts = path.split('/')
        for part in parts:
            if part == '.' or len(part) == 0:
                continue
            elif part == '..':
                if len(can_path) > 0:
                    can_path.pop()
            elif part != '/':
                can_path.append(part)
        return '/' + '/'.join(can_path)


sol = Solution()
print(sol.simplifyPath('/home/'))
print(sol.simplifyPath("/"))
print(sol.simplifyPath("/../"))



