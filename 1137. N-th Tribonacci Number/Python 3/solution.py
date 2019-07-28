class Solution:
    def tribonacci(self, n: int) -> int:
        T0, T1, T2 = 0, 1, 1
        if n == 0:
            return T0
        if n == 1:
            return T1
        if n == 2:
            return T2

        for _ in range(3, n + 1):
            T3 = T0 + T1 + T2
            T0 = T1
            T1 = T2
            T2 = T3

        return T3
