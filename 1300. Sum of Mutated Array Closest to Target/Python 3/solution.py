class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        size = len(arr)
        arr.sort()
        record = [0] * size
        record[0] = arr[0]
        for idx in range(1, size):
            record[idx] = record[idx - 1] + arr[idx]

        result = 0
        min_diff = float('inf')

        for num in range(target + 1):
            idx = bisect.bisect(arr, num)
            _sum = 0
            if idx >= 1:
                _sum += record[idx - 1]
            _sum += num * (size - idx)

            diff = abs(target - _sum)
            if diff < min_diff:
                min_diff = diff
                result = num

        return result
