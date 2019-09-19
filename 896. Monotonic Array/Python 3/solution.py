class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        size = len(A)
        sign = 0

        for idx in range(1, size):
            if A[idx] < A[idx - 1]:
                if sign == 0:
                    sign = -1
                elif sign == 1:
                    return False
            elif A[idx] > A[idx - 1]:
                if sign == 0:
                    sign = 1
                elif sign == -1:
                    return False

        return True
