class RLEIterator:

    def __init__(self, A: List[int]):
        self.A = A
        self.index = 0

    def next(self, n: int) -> int:
        if self.index >= len(self.A):
            return -1

        while self.A[self.index] < n:
            n -= self.A[self.index]
            self.A[self.index] = 0
            self.index += 2
            if self.index >= len(self.A):
                return -1

        self.A[self.index] -= n
        return self.A[self.index + 1]


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(A)
# param_1 = obj.next(n)
