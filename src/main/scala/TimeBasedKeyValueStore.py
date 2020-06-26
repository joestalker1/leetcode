from collections import defaultdict
from bisect import bisect


class TimeMap:
    def __init__(self):
        self.key_to_timestamp = defaultdict(list)

    def set(self, key, value, timestamp):
        self.key_to_timestamp[key].append((timestamp, value))

    def get(self, key, timestamp):
        map = self.key_to_timestamp.get(key,None)
        if map is None:
            return ""
        i = bisect(map, (timestamp, chr(127)))
        return map[i-1][1] if i else ""


tmap = TimeMap()
tmap.set("aaa", "aaa1", 1)
tmap.set("aaa","aaa2", 2)
print(tmap.get("aaa", 2))
print(tmap.get("aaa",1))

