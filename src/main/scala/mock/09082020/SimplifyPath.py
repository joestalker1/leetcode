class Solution:
    def simplifyPath(self, path: str) -> str:
        st = []
        arr = path.split('/')
        for part in arr:
            if not part or part == '.':
                continue
            if part == '..':
                if st:
                    st.pop()
            else:
                st.append(part)
        return '/' + '/'.join(st)
