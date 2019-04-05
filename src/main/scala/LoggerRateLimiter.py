from collections import defaultdict

class Logger:
    def __init__(self):
        self.map = defaultdict(lambda: "")

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.map:
            self.map[message] = timestamp
            return True
        t = self.map[message]
        if timestamp - t >= 10:
            self.map[message] = timestamp
            return True
        return False

logger = Logger()
print(logger.shouldPrintMessage(1, "foo"))
print(logger.shouldPrintMessage(2,"bar"))
print(logger.shouldPrintMessage(3,"foo"))
print(logger.shouldPrintMessage(8,"bar"))
print(logger.shouldPrintMessage(10, "foo"))
print(logger.shouldPrintMessage(11, "foo"))


# true,true,false,false,false,true
#["Logger","shouldPrintMessage","shouldPrintMessage","shouldPrintMessage","shouldPrintMessage","shouldPrintMessage","shouldPrintMessage"]
#[[],[1,"foo"],[2,"bar"],[3,"foo"],[8,"bar"],[10,"foo"],[11,"foo"]]
