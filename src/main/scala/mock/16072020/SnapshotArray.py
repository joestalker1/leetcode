from collections import defaultdict

class SnapshotArray:

    def __init__(self, length: int):
        self.snap_id = 0
        self.arr = [0] * length
        self.changes = defaultdict(dict)

    def set(self, index: int, val: int):
        # store changes if snap has been called
        if self.snap_id > 0:
            snap_id = self.snap_id - 1
            if snap_id not in self.changes or index not in self.changes[snap_id]:
                self.changes[snap_id][index] = self.arr[index]
        self.arr[index] = val

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int):
        if snap_id in self.changes and index in self.changes[snap_id]:
            return self.changes[snap_id][index]
        else:
            if len(self.changes.keys()) > 0:
                for k in self.changes.keys():
                    if k > snap_id and index in self.changes[k]:
                        return self.changes[k][index]
            return self.arr[index]

#["SnapshotArray","snap","get","get","snap","set", "set", "set","set","get","set"]
#  [[1],           [],   [0,0],[0,0],  [],  [0,11],[0,12],[0,2],[0,3],[0,1],[0,11]]

#["SnapshotArray","set","snap","set","get"]
# [[3],[0,5],[],[0,6],[0,0]]
sa = SnapshotArray(3)
sa.set(0, 5)
sa.snap()
sa.set(0, 6)
print(sa.get(0, 0))

sa = SnapshotArray(1)
sa.snap() # snap_id = 0
print(sa.get(0, 0))
print(sa.get(0, 0))
sa.snap() #sanp_id = 1
sa.set(0,11)
sa.set(0,12)
sa.set(0,2)
sa.set(0, 3)
print(sa.get(0, 1))
sa.set(0,11)
