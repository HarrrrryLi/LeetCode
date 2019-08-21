class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        size = len(difficulty)
        sorted_d = sorted(
            [(d, idx) for idx, d in enumerate(difficulty)], key=lambda x: x[0])

        dp = [0] * (size + 1)
        result = 0

        for idx in range(1, size + 1):
            d, i = sorted_d[idx - 1]
            dp[idx] = max(dp[idx - 1], profit[i])

        for w in worker:
            idx = bisect.bisect_right(sorted_d, (w, size))
            result += dp[idx]

        return result
