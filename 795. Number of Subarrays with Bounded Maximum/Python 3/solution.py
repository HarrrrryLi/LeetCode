class Solution:
    def numSubarrayBoundedMax(self, A: List[int], L: int, R: int) -> int:
        stop = []
        nums = []
        size = len(A)

        for idx, num in enumerate(A):
            if num >= L and num <= R:
                nums.append(idx)
            elif num > R:
                stop.append(idx)

        stop.insert(0, -1)
        stop.append(size)
        result = 0

        for index in nums:
            i = bisect.bisect(stop, index)
            right = max(0, stop[i] - index - 1)
            left = max(0, index - stop[i - 1] - 1)
            result += (left + 1) * (right + 1)
            stop.insert(i, index)

        return result
