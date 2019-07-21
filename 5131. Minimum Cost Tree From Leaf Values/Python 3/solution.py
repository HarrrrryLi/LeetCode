class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        cached = {}
        return self.helper(arr, cached)

    def helper(self, arr, cached):
        size = len(arr)
        if size == 2:
            return arr[0] * arr[1]
        if size == 1:
            return 0

        result = float('inf')
        for idx in range(1, size):
            left, right = arr[:idx], arr[idx:]
            left_set, right_set = tuple(left), tuple(right)
            cur = max(left) * max(right)
            if cur >= result:
                continue
            if left_set in cached:
                left_value = cached[left_set]
            else:
                left_value = self.helper(left, cached)
                cached[left_set] = left_value

            if right_set in cached:
                right_value = cached[right_set]
            else:
                right_value = self.helper(right, cached)
                cached[right_set] = right_value
            total = cur + left_value + right_value
            result = min(result, total)

        return result
