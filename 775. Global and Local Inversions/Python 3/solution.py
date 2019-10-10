class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        size = len(A)
        min_value = A[-1]
        for idx in range(size - 3, -1, -1):
            min_value = min(min_value, A[idx + 2])
            if A[idx] > min_value:
                return False

        return True
