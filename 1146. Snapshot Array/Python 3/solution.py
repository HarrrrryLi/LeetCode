class SnapshotArray:

    def __init__(self, length: int):
        self.snap_dict = {}
        self.snap_id = 0

        for cnt in range(length):
            self.snap_dict[(self.snap_id, cnt)] = 0

    def set(self, index: int, val: int) -> None:
        self.snap_dict[(self.snap_id, index)] = val

    def snap(self) -> int:
        temp = self.snap_id
        self.snap_id += 1

        return temp

    def get(self, index: int, snap_id: int) -> int:

        while snap_id >= 0:
            if (snap_id, index) in self.snap_dict:
                return self.snap_dict[(snap_id, index)]
            snap_id -= 1

        return 0


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
