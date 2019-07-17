class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        size = len(A)
        max_values = [A[-1]]
        result = 0
        for cnt in range(size - 2, -1, -1):
            max_values.insert(0, max(max_values[0], A[cnt]))

        # print(max_values)

        right = 0
        left = 0
        while right < size:
            while left < right and A[left] > max_values[right]:
                left += 1

            result = max(right - left, result)
            right += 1

        return result
