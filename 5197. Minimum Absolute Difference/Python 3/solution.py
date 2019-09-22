class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        size = len(arr)
        min_diff = float('inf')
        result = []
        for idx, num in enumerate(arr):
            if idx >= 1:
                diff = num - arr[idx - 1]
                if diff == min_diff:
                    result.append([arr[idx - 1], num])
                if diff < min_diff:
                    min_diff = diff
                    result = [[arr[idx - 1], num]]
        return result
