class Log:
    def __init__(self, s):
        parts = s.split(':')
        self.func_id = int(parts[0])
        self.timestamp = int(parts[2])
        self.is_start = parts[1] == 'start'


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        # assert self._exclusiveTime(1, ['0:start:0','0:end:1']) == [2], 'test1'
        # assert self._exclusiveTime(1, ['0:start:0','0:end:1']) == [2], 'test2'
        # assert self._exclusiveTime(1, ['0:start:0','0:start:1','0:end:2']) == [3], 'test3'
        return self._exclusiveTime(n, logs)

    def _exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        id_to_time = [0] * n
        for s in logs:
            log = Log(s)
            if log.is_start:
                stack.append(log)
            else:
                top = stack.pop()
                exec_time = log.timestamp - top.timestamp + 1
                id_to_time[log.func_id] += exec_time
                # to avoid count exec_time twice
                if stack:
                    id_to_time[stack[-1].func_id] -= exec_time
        return id_to_time
    