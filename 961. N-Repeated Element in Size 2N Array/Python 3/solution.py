class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        if A[0] == A[-1] or A[-1] == A[-2]:
            return A[-1]

        size = len(A)

        for cnt in range(size - 2):
            if A[cnt] == A[cnt + 1] or A[cnt] == A[cnt + 2]:
                return A[cnt]

        return -1
