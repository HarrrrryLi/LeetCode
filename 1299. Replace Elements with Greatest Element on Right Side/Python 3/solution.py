class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        size = len(arr)
        result = [0] * size
        result[-1] = -1

        for cnt in range(size - 1, 0, -1):
            result[cnt - 1] = max(result[cnt], arr[cnt])

        return result
