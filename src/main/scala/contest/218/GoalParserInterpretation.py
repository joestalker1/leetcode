class Solution:
    def interpret(self, command):
        if not command:
            return command
        cmd_to_char = {"G":"G","()": "o","(al)":"al"}
        st = []
        res = []
        for ch in command:
            if ch == "G":
                res.append(cmd_to_char[ch])
            elif ch == "(":
                st.append(ch)
            elif ch == ")":
                st.append(ch)
                res.append(cmd_to_char[''.join(st)])
                st = []
            else:
                st.append(ch)
        return ''.join(res)
