class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        if not S and not T:
            return True
        if not S or not T:
            return False

        def apply_backspace(s):
            bk = 0
            j = len(s) - 1
            while j >= 0:
                if s[j] == "#":
                    bk += 1
                    s.pop(j)
                    j -= 1
                else:
                    if bk > 0:
                        while j >= 0 and bk > 0 and s[j] != '#':
                            s.pop(j)
                            j -= 1
                            bk -= 1
                    else:
                        j -= 1
            return s

        S = apply_backspace(list(S))
        T = apply_backspace(list(T))
        return S == T


sol = Solution()
print(sol.backspaceCompare("ab##", "c#d#"))
print(sol.backspaceCompare("ab#c", "ad#c"))
print(sol.backspaceCompare("bxj##tw", "bxo#j##tw"))#true



