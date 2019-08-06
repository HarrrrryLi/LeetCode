class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        if N >= K + W:
            return 1.0
        if N < K:
            return 0.0

        dp = [0] * (K + W)
        for cnt in range(K, N + 1):
            dp[cnt] = 1
        density = 1 / W
        tmp = N + 1 - K

        for cnt in range(K - 1, -1, -1):
            dp[cnt] = tmp * density
            tmp += dp[cnt] - dp[cnt + W]
        return dp[0]
