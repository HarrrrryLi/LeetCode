class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        if not A:
            return 0

        result = 0
        A.sort()
        size = len(A)

        for idx in range(1, size):
            num = A[idx]
            if num <= A[idx - 1]:
                A[idx] = A[idx - 1] + 1
                result += A[idx] - num

        return result
