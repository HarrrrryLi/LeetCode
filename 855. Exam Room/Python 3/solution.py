class ExamRoom:

    def __init__(self, N: int):
        self.seated = []
        self.total = N

    def seat(self) -> int:
        if not self.seated:
            self.seated.append(0)
            return 0
        size = len(self.seated)
        if size == 1:
            if self.seated[0] >= self.total - 1 - self.seated[0]:
                self.seated.insert(0, 0)
                return 0
            else:
                self.seated.append(self.total - 1)
                return self.total - 1
        else:
            max_dist = self.seated[0]
            max_seat = 0
            insert_idx = 0
            for idx in range(1, size):
                seat = (self.seated[idx] + self.seated[idx - 1]) // 2
                dist = (self.seated[idx] - self.seated[idx - 1]) // 2
                if dist > max_dist:
                    max_dist = dist
                    max_seat = seat
                    insert_idx = idx

            if self.total - 1 - self.seated[-1] > max_dist:
                max_seat = self.total - 1
                insert_idx = size

            self.seated.insert(insert_idx, max_seat)

            return max_seat

    def leave(self, p: int) -> None:
        for idx in range(len(self.seated)):
            if self.seated[idx] == p:
                self.seated.pop(idx)
                break


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(N)
# param_1 = obj.seat()
# obj.leave(p)
