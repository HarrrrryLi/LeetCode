import collections


class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.data = collections.deque()
        self.size = size
        self.sum = 0

    def next(self, val: int) -> float:
        self.data.append(val)
        self.sum += val

        if len(self.data) > self.size:
            self.sum -= self.data.popleft()

        return self.sum / len(self.data)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
