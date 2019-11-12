class Solution(object):
    def addOperators(self, num, target):
        if not num:
            return []
        res = []

        def calc_exp(pos, prev_operand, cur_operand, value, buf):
            if pos == len(num):
                if value == target and cur_operand == 0:
                    res.append(''.join(buf[1:]))
                return
            cur_operand = cur_operand * 10 + int(num[pos])
            if cur_operand > 0:
                calc_exp(pos + 1, prev_operand, cur_operand, value, buf)
            str_oper = str(cur_operand)
            # +
            buf.append('+')
            buf.append(str_oper)
            calc_exp(pos + 1, cur_operand, 0, value + cur_operand, buf)
            buf.pop()
            buf.pop()

            if buf:
                # -
                buf.append('-')
                buf.append(str_oper)
                calc_exp(pos + 1, -cur_operand, 0, value - cur_operand, buf)
                buf.pop()
                buf.pop()

                # *
                buf.append('*')
                buf.append(str_oper)
                calc_exp(pos + 1, prev_operand * cur_operand, 0, value - prev_operand + prev_operand * cur_operand, buf)
                buf.pop()
                buf.pop()
        calc_exp(0, 0, 0, 0, [])
        return res





sol = Solution()
#print(sol.addOperators(num = "3456237490", target = 9191))
#print(sol.addOperators(num = "00", target = 0))
#print(sol.addOperators(num = "105", target = 5))
print(sol.addOperators(num = "123", target = 6))
#print(sol.addOperators(num = "232", target = 8))









