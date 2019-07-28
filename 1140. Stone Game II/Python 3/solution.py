class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        size = len(piles)
        dp = [0] * size
        dp[0] = piles[0]
        for cnt in range(1, size):
            dp[cnt] = dp[cnt - 1] + piles[cnt]
        dp.insert(0, 0)

        d = {}
        result, _ = self.helper(dp, 1, 1, d)
        return result

    def helper(self, dp, M, start, d):
        size = len(dp)
        if size - start <= 2 * M:
            rest = dp[size - 1] - dp[start - 1]
            return rest, 0

        result = (-1, -1)
        for x in range(1, 2 * M + 1):
            _sum = dp[start + x - 1] - dp[start - 1]
            nxtM = max(x, M)
            if (start + x, nxtM) in d:
                nxt, this = d[(start + x, nxtM)]
            else:
                nxt, this = self.helper(dp, nxtM, start + x, d)
                d[(start + x, nxtM)] = (nxt, this)
            _sum += this
            if _sum > result[0]:
                result = (_sum, nxt)

        return result
