class Solution:
    def evaluate(self, s: str, knowledge):
        if not s or not knowledge:
            return None
        key_to_word = {k:v for k,v in knowledge}
        buf = []
        i = 0
        while i < len(s):
            if s[i] == '(':
                key = []
                i += 1
                while s[i] != ')':
                    key.append(s[i])
                    i += 1
                i += 1
                word = key_to_word.get(''.join(key), '?')
                buf.append(word)
            else:
                buf.append(s[i])
            i += 1
        return ''.join(buf)


sol = Solution()
print(sol.evaluate("(name)is(age)yearsold", [["name","bob"],["age","two"]]))


