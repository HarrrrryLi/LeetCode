class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        size = len(arr)
        diff = (arr[-1] - arr[0]) // size

        for idx in range(1, size):
            if arr[idx] != arr[idx - 1] + diff:
                return arr[idx - 1] + diff

        return arr[-1] - diff
