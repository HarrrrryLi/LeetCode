class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        size = len(arr)
        dp = [{} for _ in range(size)]

        dp[0][True] = 0
        dp[0][False] = arr[0]

        result = arr[0]

        for idx in range(1, size):
            dp[idx][True] = dp[idx - 1][True] + arr[idx]
            dp[idx][False] = dp[idx - 1][False] + arr[idx]
            if idx >= 2:
                dp[idx][True] = max(
                    dp[idx][True], dp[idx - 2][False] + arr[idx])
            dp[idx][False] = max(dp[idx][False], arr[idx])

            result = max(dp[idx][True], dp[idx][False], result)

        return result
