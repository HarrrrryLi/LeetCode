class Solution:
    def numTilings(self, N: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [1, 0, 0, 0]
        for _ in range(N):
            ndp = [0, 0, 0, 0]
            ndp[0] = (dp[0] + dp[3]) % MOD
            ndp[1] = (dp[0] + dp[2]) % MOD
            ndp[2] = (dp[0] + dp[1]) % MOD
            ndp[3] = (dp[0] + dp[1] + dp[2]) % MOD
            dp = ndp

        return dp[0]
