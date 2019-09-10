class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        return self.sumOrd(s1) + self.sumOrd(s2) - self.maxCommonSubsequenceDP(s1, s2)

    def maxCommonSubsequenceDP(self, s1: str, s2: str) -> int:
        size1, size2 = len(s1), len(s2)

        if size1 == 0 or size2 == 0:
            return 0
        dp = [[0] * (size2 + 1) for _ in range(size1 + 1)]
        for cnt1 in range(1, size1 + 1):
            for cnt2 in range(1, size2 + 1):
                if s1[cnt1 - 1] == s2[cnt2 - 1]:
                    dp[cnt1][cnt2] = dp[cnt1 - 1][cnt2 - 1] + \
                        ord(s1[cnt1 - 1]) * 2
                else:
                    dp[cnt1][cnt2] = max(
                        dp[cnt1][cnt2 - 1], dp[cnt1 - 1][cnt2])
        return dp[-1][-1]

    def sumOrd(self, s: str) -> int:
        result = 0
        for c in s:
            result += ord(c)
        return result
