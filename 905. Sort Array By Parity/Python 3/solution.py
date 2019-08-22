class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:

        size = len(A)
        left, right = 0, size - 1

        while left < right:
            while left < right and A[left] % 2 == 0:
                left += 1

            while right > left and A[right] % 2 == 1:
                right -= 1

            A[left], A[right] = A[right], A[left]

        return A
