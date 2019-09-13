class Solution:
    def findIntegers(self, num: int) -> int:
        dp = [0] * 31
        dp[0] = 1
        dp[1] = 2
        for i in range(2, 31):
            dp[i] = dp[i - 1] + dp[i - 2]

        i, s, pre = 30, 0, 0
        while i >= 0:
            if (num & (1 << i)) != 0:
                s += dp[i]
                if pre == 1:
                    s -= 1
                    break
                pre = 1
            else:
                pre = 0
            i -= 1
        return s + 1
