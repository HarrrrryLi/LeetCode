class Solution:
    def distinctSubseqII(self, S: str) -> int:
        size = len(S)
        dp = [0] * size
        visited = set()

        for idx, c in enumerate(S):
            if c not in visited:
                visited.add(c)
                dp[idx] = 1

        for idx in range(size):
            visited = set()
            for nxt in range(idx + 1, size):
                if S[nxt] not in visited:
                    visited.add(S[nxt])
                    dp[nxt] += dp[idx]

        return sum(dp) % (10 ** 9 + 7)
