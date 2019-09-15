class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:

        size = len(arr)
        dp = [0] * size
        dp[0] = arr[0]
        _sum = [0] * size
        _sum[0] = arr[0]

        for cnt in range(1, size):
            dp[cnt] = max(dp[cnt - 1], 0) + arr[cnt]
            _sum[cnt] = _sum[cnt - 1] + arr[cnt]

        result = max(0, max(dp))
        max_sum = max(_sum)
        if k > 1 and _sum[-1] > 0:
            result = max(result, dp[-1] + (k - 2) * _sum[-1] + max_sum)
        if k > 1:
            result = max(result, dp[-1] + max_sum)

        return result % (10 ** 9 + 7)
