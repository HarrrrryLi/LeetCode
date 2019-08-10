class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        size = len(arr)
        min_list = [0] * size
        max_list = [0] * size

        min_list[-1] = arr[-1]
        max_list[0] = arr[0]

        for idx in range(1, size):
            min_value = min(arr[-1 - idx], min_list[-idx])
            max_value = max(arr[idx], max_list[idx - 1])
            min_list[-1 - idx] = min_value
            max_list[idx] = max_value
        result = 1
        for idx in range(size - 1):
            if min_list[idx + 1] >= max_list[idx]:
                result += 1

        return result