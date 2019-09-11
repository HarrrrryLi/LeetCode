class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        size = len(s)
        dp = [0] * (size + 1)
        dp[0] = 1
        if s[0] == '*':
            dp[1] = 9
        else:
            dp[1] = 1

        for idx in range(1, size):
            if s[idx] != '0':
                if s[idx] == '*':
                    dp[idx + 1] += dp[idx] * 9
                else:
                    dp[idx + 1] += dp[idx]
            if s[idx - 1] == '1':
                if s[idx] == '*':
                    dp[idx + 1] += dp[idx - 1] * 9
                else:
                    dp[idx + 1] += dp[idx - 1]
            elif s[idx - 1] == '2':
                if s[idx] == '*':
                    dp[idx + 1] += dp[idx - 1] * 6
                elif int(s[idx]) <= 6:
                    dp[idx + 1] += dp[idx - 1]
            elif s[idx - 1] == '*':
                if s[idx] == '*':
                    dp[idx + 1] += dp[idx - 1] * 15
                elif int(s[idx]) <= 6:
                    dp[idx + 1] += dp[idx - 1] * 2
                else:
                    dp[idx + 1] += dp[idx - 1]

        return dp[-1] % (10 ** 9 + 7)
