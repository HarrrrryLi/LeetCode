class Solution:
    def numPermsDISequence(self, S: str) -> int:
        size = len(S) + 1
        dp = [[0] * size for _ in range(size)]
        dp[0][0] = 1
        for i in range(1, size):
            for j in range(i + 1):
                if S[i - 1] == 'D':
                    for k in range(j, i):
                        dp[i][j] += dp[i - 1][k]
                elif S[i - 1] == 'I':
                    for k in range(j):
                        dp[i][j] += dp[i - 1][k]
        return sum(dp[-1]) % (10 ** 9 + 7)
