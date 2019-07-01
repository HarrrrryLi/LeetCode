class Solution:
    def fib(self, N: int) -> int:
        if N == 0:
            return 0
        if N == 1:
            return 1

        last2 = 0
        last1 = 1
        current = 0
        for _ in range(2, N + 1):
            current = last2 + last1
            last2 = last1
            last1 = current

        return current
