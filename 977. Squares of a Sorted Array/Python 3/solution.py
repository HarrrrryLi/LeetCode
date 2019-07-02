class Solution:
    def sortedSquares(self, A: list[int]) -> list[int]:

        #         size = len(A)
        #         left = 0
        #         right = size - 1

        #         result = []

        #         while left <= right:
        #             if abs(A[left]) >= abs(A[right]):
        #                 result.insert(0, A[left] * A[left])
        #                 left += 1
        #             else:
        #                 result.insert(0, A[right] * A[right])
        #                 right -= 1

        #         return result
        return sorted([a * a for a in A])
