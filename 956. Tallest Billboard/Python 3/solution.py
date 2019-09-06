class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        dp = collections.defaultdict(int)
        dp[0] = 0
        # For each value in rods, we consider adding, subtracting or not including the value
        # Key = how balanced (ie, -6 + 6), Value = total weight
        # answer is dp[0] because 0 means we have equal number of + and - values
        # For each value of a weight, the maximum weight you can have is the
        for r in rods:
            nextlevel = collections.defaultdict(int)
            for cursum, totalweight in dp.items():
                nextlevel[cursum +
                          r] = max(nextlevel[cursum + r], totalweight + r)
                nextlevel[cursum] = max(nextlevel[cursum], totalweight)
                nextlevel[cursum -
                          r] = max(nextlevel[cursum - r], totalweight + r)
            dp = nextlevel
        return dp[0] // 2
