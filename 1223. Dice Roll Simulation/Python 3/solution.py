class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        mod = 10 ** 9 + 7
        dp = [[0, 1] + [0] * 14 for _ in range(6)]
        for _ in range(n - 1):
            nxt = [[0] * 16 for i in range(6)]
            for i in range(6):
                for k in range(1, rollMax[i] + 1):
                    for j in range(6):
                        if i == j:
                            if k < rollMax[i]:
                                nxt[j][k + 1] += dp[i][k] % mod
                        else:
                            nxt[j][1] += dp[i][k] % mod
            dp = nxt
        return sum(sum(row) for row in dp) % mod
