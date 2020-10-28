class Logger:

    def __init__(self):
        self.msg_to_time = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.msg_to_time:
            self.msg_to_time[message] = timestamp
            return True
        printed_at = self.msg_to_time[message]
        if timestamp - printed_at >= 10:
            self.msg_to_time[message] = timestamp
            return True
        return False

